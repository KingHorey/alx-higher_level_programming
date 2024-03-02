#!/usr/bin/python3

""" import urllib """
import urllib.request

url = "https://alx-intranet.hbtn.io/status"
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    content = response.read()
    print("- type: {}$".format(type(content)))
    print("- content: {}$".format(content))
    print("- utf8 content: {}$".format(content.decode('utf-8')))
