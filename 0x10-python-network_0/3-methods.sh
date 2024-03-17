#!/bin/bash
# ASK SERVER TO RETURN A LIST OF METHODS IT SUPPORTS
curl -sI --request OPTIONS "$1" | grep "allow" | cut -d ":" -f 2
