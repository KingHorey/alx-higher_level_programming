#!/bin/bash
# This script will print the size of the body of the response
curl --head -s "$1" | grep "Content-Length" | awk '{print $2}'
