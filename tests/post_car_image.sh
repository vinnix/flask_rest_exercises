#!/bin/env bash

file_path="./"
file_name="chinese-dragon.png"
host_addr="http://127.0.0.1:5100"
method="/api/submit"

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







curl -i -X POST -H "Content-Type: multipart/mixed" -F "file=@${file_path}${file_name}" \
    -F  "{
            \"carname\": \"$car\",
            \"company\": \"$company\"
        };type=application/json" \
     http://localhost:5100/cars


exit

## 302 means the test was OK, so we can supress the output
## Otherwise we show error message with the complete output
## Alternatively, for the next version we could check the md5/sha256
## with the .png file and the one found on the other side

if [[ $RESULT =~ "302" ]];
then
    echo "SUCESS!"
    echo "Upload done!"
else
    echo "!!! ERROR !!!"
    echo "Full output:"
    echo ${RESULT}
fi
