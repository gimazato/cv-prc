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
    -v $(pwd):/work \
    -w /work \
    --name $(whoami)_`date "+%Y%m%d_%H%M%S"` \
    "keras-tf2.2":"v3" \
    "python3 video-gamma.py"
    #"bash"
    #"python3 check_load_weight.py"
    #"python3 check_using_gpu.py | grep device"