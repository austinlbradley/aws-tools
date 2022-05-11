#!/bin/bash

INSTANCES=(
    i-0abcdef1234567890,
    i-01234567890abcdef)
ROLE=default

for (( i=0; i<${#instances[@]}; i++ )); do
    
    aws-vault exec $ROLE -- aws ec2 describe-instances --instance-ids ${INSTANCES[$i]} | jq
    
    # lines below parse json and prints the tags for each instance
    # echo InstanceID: ${INSTANCES[$i]}
    # aws-vault exec $ROLE -- aws ec2 describe-instances --instance-ids ${INSTANCES[$i]} | jq '. | .Reservations[0].Instances[0].Tags[]'

done