#!/bin/env bash


file_path="./"
file_name="chinese-dragon.png"
host_addr="172.17.0.2:5100"
method="/api/submit"

curl -X PUT -T "${file_path}${file_name}" "${host_addr}${method}"

