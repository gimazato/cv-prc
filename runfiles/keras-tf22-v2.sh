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
    -u $USER_ID:$USER_GROUP \
    --name $(whoami)_`date "+%Y%m%d_%H%M%S"` \
    "keras-tf2.2":"v2" \
    python3 hello.py