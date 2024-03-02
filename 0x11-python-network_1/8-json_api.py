#!/usr/bin/python3

""" import requests and sys """
import requests
import sys


def send_mail_get_json():
    """ sends a POST request to server """

    if len(sys.argv) == 1:
        q = ""
    elif len(sys.argv) > 1:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}

    response = requests.post(url, data)
    try:
        response = response.json()
        if response:
            print("{[]} {}".format(response.get('id'), response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    send_mail_get_json()
