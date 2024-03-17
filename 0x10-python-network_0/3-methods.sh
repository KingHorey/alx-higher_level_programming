#!/bin/bash
# ASK SERVER TO RETURN A LIST OF METHODS IT SUPPORTS
curl -sI --request OPTIONS "$1" | grep -i "Allow" | cut -d ":" -f 2
