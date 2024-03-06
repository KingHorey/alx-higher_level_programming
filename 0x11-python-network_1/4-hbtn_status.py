#!/usr/bin/python3

""" import requests """
import requests


def status():
    """ function that fetches https://alx-intranet.hbtn.io/status"""
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    status()
