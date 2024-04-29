#!/bin/env bash


re='^[0-9]+$'
if [[ "$1" =~ $re  ]];
then
    id=$1
else
    echo "Your 1st parameter must be a number. Id of Car."
    echo "Existing the test."
    exit
fi



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



put_update_car(){
    curl -X PUT  http://localhost:5100/record/$id \
        -H 'Content-Type: application/json' \
        -d "{
            \"carname\": \"$car\",
            \"company\": \"$company\"
        }"
}



put_update_car;

