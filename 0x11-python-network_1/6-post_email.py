#!/usr/bin/python3

""" import requests and sys modules """
import requests
import sys


def sendMail():
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    response = requests.post(url, data)

    print(response.text)


if __name__ == "__main__":
    sendMail()
