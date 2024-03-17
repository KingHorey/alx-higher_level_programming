#!/bin/bash
# ASK SERVER TO RETURN A LIST OF METHODS IT SUPPORTS
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
