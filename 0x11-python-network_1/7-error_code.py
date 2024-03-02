#!/usr/bin/python3

""" import requests and sys """
import requests
import sys


def try_request():
    """ function tries to make connection to url """
    try:
        url = sys.argv[1]
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except HTTPError as e:
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))


if __name__ == "__main__":
    try_request()
