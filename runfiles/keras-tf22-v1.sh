#!/bin/bash
# Get user id, group, name
USER_ID=$(id -u)
USER_GROUP=$(id -g)
USER_NAME=docker_$(id -u -n)

# run docker container
docker run \
    --rm -it \
    --gpus all \
    -e USER_ID=$USER_ID \
    -e GROUP_ID=$USER_GROUP \
    -e USER_NAME=$USER_NAME \
    -v $(pwd):/home/work \
    -w /home/work \
    --name $(whoami)_`date "+%Y%m%d_%H%M%S"` \
    "keras-tf2.2":"v1" \
    su $USER_NAME