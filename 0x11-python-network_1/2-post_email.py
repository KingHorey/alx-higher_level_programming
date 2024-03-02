#!/usr/bin/python3

""" import urllib and sys """
import urllib.request
import urllib.parse
import sys


def sendMail():
    """ makes a POST request to the URL provided with the email """
    url = sys.argv[1]
    email = {
            'email': sys.argv[2]
            }
    email = urllib.parse.urlencode(email)
    email = email.encode('ascii')
    req = urllib.request.Request(url, email)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))


if __name__ == "__main__":
    sendMail()
