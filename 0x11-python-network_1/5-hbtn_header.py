#!/usr/bin/python3

""" import requests """
import requests
import sys


def getHeader():
    """ gets header variable """
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))


if __name__ == "__main__":
    getHeader()
