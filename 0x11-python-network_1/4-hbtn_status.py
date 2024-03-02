#!/usr/bin/python3

""" import requests """
import requests


def runRequests():
    """ get the response from the server """
    response = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    runRequests()
