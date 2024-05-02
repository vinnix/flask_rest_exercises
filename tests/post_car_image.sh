#!/bin/env bash

file_path="./"
file_name="chinese-dragon.png"
host_addr="127.0.0.1"
port=5100
method="multi_add"

if [[ "$2" == "" ]];
then
        car=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 13; echo)
    else
            car="$2"
fi

if [[ "$3" == "" ]];
then
        company=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 13; echo)
    else
            company="$3"
fi



curl -X POST -H "Content-Type: multipart/form-data" \
     -F "file=<chinese-dragon.png" \
     -F "json_data={\"carname\":\"$car\",\"company\":\"$company\"}" \
     http://$host_addr:$port/$method


