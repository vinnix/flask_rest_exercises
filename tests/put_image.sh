#!/bin/env bash

file_path="./"
file_name="chinese-dragon.png"
host_addr="http://127.0.0.1:5100"
method="/api/submit"

RESULT=$( curl -i -X POST -H "Content-Type: multipart/form-data" -F "file=@${file_path}${file_name}" "${host_addr}${method}")

if [[ $RESULT =~ "302" ]];
then
    echo "SUCESS!"
    echo "Upload done!"
else
    echo "!!! ERROR !!!"
    echo "Full output:"
    echo ${RESULT}
fi
