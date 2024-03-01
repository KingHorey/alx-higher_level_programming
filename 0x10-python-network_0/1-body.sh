#!/bin/bash
# Prints the body of the response
response=$(curl -s -o /dev/null -w "%{http_code}" "$1"); [ "$response" -eq 200 ] && curl -s -X GET "$1"
