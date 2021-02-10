#!/bin/bash

# CONFIGURATION
# Shell user to execute commands on HDFS
HDSF_USER="hdfs"

# FUNCTIONS

function hdfs_set_group_acl() {

  echo "[HDFS] Setting ACL: ${ACL} for group: ${NAME} for folder: ${PATH}"
  ACL_SPEC=$(echo "${ACL_TYPE}:${NAME}:${ACL} ${PATH}")

  echo "sudo -u $HDSF_USER hdfs dfs -setfacl -m $ACL_SPEC"
  # sudo -u $HDSF_USER hdfs dfs -setfacl -m $ACL_SPEC $ARG3
}



# MAIN
# SUPPORTED_COMMANDS="show-acl set-group-acl remove-group-acl set-user-acl remove-user-acl"
# COMMAND=$1
ACL_TYPE=$1 # acl type e.g. group, default
NAME=$2 # user/group name
PATH=$3 # path
ACL=$4 # acl e.g. rwx

hdfs_set_group_acl
