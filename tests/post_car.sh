#!/bin/env bash


if [[ "$2" == "" ]];
then
    car=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 13; echo)
else
    company="$2"
fi

if [[ "$3" == "" ]];
then
    company=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 13; echo)
else
        car="$3"
fi



post_new_car(){
    curl -X POST  http://localhost:5100/cars \
        -H 'Content-Type: application/json' \
        -d "{
            \"carname\": \"$car\",
            \"company\": \"$company\"
        }"
}



post_new_car;

if [[ "$1" == "duplicate" ]];
then

    post_new_car;

fi
