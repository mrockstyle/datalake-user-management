import yaml
import subprocess


CONFIG_FILE = "config/dlake_user.yaml"
HDFS_SCRIPT = "shell-scripts/hdfs-script.sh"

# CONFIGURATION KEY

GROUPS_KEY = "groups"
GROUP_KEY = "group"
NAME_KEY = "name"
IGNORE_KEY = "ignore"
HDFS_KEY = "hdfs"
HIVE_KEY = "hive"
HBASE_KEY = "hbase"
HDFS_PATH = "path"
HDFS_ACL = "permission"
HDFS_RECURSIVE = "recursive"
HDFS_ACL_TYPE = "type"



def read_groups_config_file(config_file):
    group_list = []

    with open(config_file, 'r') as file:

        yaml_file = yaml.safe_load(file)
        for group in yaml_file[GROUPS_KEY]:
            group_list.append(group[GROUP_KEY])

    return group_list

def create_group(config_file):

    group_list = read_groups_config_file(config_file)

    for group in group_list:

        group_name = group[NAME_KEY]

        if IGNORE_KEY in group.keys() and group[IGNORE_KEY]:
            print("ignoring group ", group[NAME_KEY])
            continue

        if HDFS_KEY in group.keys():
            hdfs_create_group(group_name, group[HDFS_KEY])
        
        # if HIVE_KEY in group.keys():
        #     print("Have Hive")

        # if HBASE_KEY in group.keys():
        #     print("Have HBase")


def hdfs_create_group(group_name, group):

    for hdfs in group:
        for acl_type in hdfs[HDFS_ACL_TYPE]:
            hdfs_path = hdfs[HDFS_PATH]
            hdfs_acl = hdfs[HDFS_ACL]

            set_acl_permission_args = [HDFS_SCRIPT, acl_type, group_name, hdfs_path, hdfs_acl]
            shell_script_execution(set_acl_permission_args)
            # print(set_acl_permission_args)
            print("")


def shell_script_execution(process_args):

    exit_code = subprocess.call(process_args)
    if exit_code == 0:
        print("Script execution successful")
    else:
        print("Script execution failed with code ", exit_code)
    

    



# def hdfs_create_user(acl_type, name, permission, path, recursive):

#     if recursive:
#         print("sudo -u hdfs hdfs dfs -setfacl -R -m {}:{}:{} {}".format(acl_type, name, permission, path))
#     else:
#         print("sudo -u hdfs hdfs dfs -setfacl -m {}:{}:{} {}".format(acl_type, name, permission, path))


# def hive_grant_user(role_name, table_name, hive_permission):

#     for perm in hive_permission:
#         print("grant {2} on database {1} to role {0};".format(role_name, table_name, perm))


# def hbase_grant_user(user_name, ):

#     grant '<user-or-group>','<permissions>','<table>






###### MAIN ########

create_group(CONFIG_FILE)










# with open(r'/Users/sirawich/Desktop/dlake_user.yaml') as file:

#     yaml_file = yaml.load(file, Loader=yaml.FullLoader)
#     group_list = yaml.dump(yaml_file, sort_keys=False)
#     # print(group_list)

#     # print("")
#     # print("loop")
#     # print("")

#     for group_id in range(len(yaml_file['groups'])):
#         name = yaml_file['groups'][group_id]['group']['name']
#         ignore = yaml_file['groups'][group_id]['group']['ignore']
#         # Check ignore (already implement)
#         if ignore:
#             continue
        
#         print(name)
#         print("HDFS permission:")
#         for _ in yaml_file['groups'][group_id]['group']['hdfs']:
            
#             if _['recursive']:
#                 recursive = "recursive"

#             permission = _['permission']
#             path = _['path']

#             for acl_type in _['type']:
#                 # generate command   
#                 hdfs_create_user(acl_type, name, permission, path, recursive)

#         print("")
#         print("Hive permission:")
#         # print(yaml_file['groups'][group_id]['group']['hive']['role_name'])
#         for _ in yaml_file['groups'][group_id]['group']['hive']['tables']:
#             table_name = _['name']
#             hive_permission = _['permission']
#             # generate hive command
#             hive_grant_user(name, table_name, hive_permission)
           
   
#         print("")



