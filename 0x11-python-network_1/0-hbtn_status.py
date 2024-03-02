#!/usr/bin/python3

""" import urllib """
import urllib.request

url = "https://alx-intranet.hbtn.io/status"
req = urllib.request.Request(url)
def getContent():
    """ Get the content of the url """
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("- type: {}$".format(type(content)))
        print("- content: {}$".format(content))
        print("- utf8 content: {}$".format(content.decode('utf-8')))

if __name__ == "__main__":
    getContent()
