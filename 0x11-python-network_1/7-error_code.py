#!/usr/bin/python3

""" import requests and sys """
import requests
import sys


def try_request():
    """ function tries to make connection to url """
    url = sys.argv[1]
    try:
        response = requests.get(url)
        print(response.text)
    except requests.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))


if __name__ == "__main__":
    try_request()
