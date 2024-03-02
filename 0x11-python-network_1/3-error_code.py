#!/usr/bin/python3

""" import urllib """
import urllib.request
from urllib.error import HTTPError
import sys


def showErrorCode():
    """ return an error code on failure """
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    showErrorCode()
