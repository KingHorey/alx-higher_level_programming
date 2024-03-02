#!/usr/bin/python3

""" import urllib """
import urllib.request
import sys


def getHeader():
    """ get X-Request-Id header value """
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        content = response.getheader('X-Request-Id')
        print(content)


if __name__ == "__main__":
    getHeader()
