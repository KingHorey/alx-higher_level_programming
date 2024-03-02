#!/usr/bin/python3

""" import requests """
import requests


def runresponse():
    """ get the response from the server """
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    runresponse()
