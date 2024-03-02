#!/usr/bin/python3

""" import requests module """
import requests
from sys import argv


def getGithubAPI():
    """ get github api """
    url = 'https://api.github.com/user'
    user = argv[1]
    password = argv[2]
    headers = {'Authorization': 'token {}'.format(password)}
    response = requests.get(url, headers=headers, params={'username': user})
    print(response.json().get('id'))


if __name__ == '__main__':
    getGithubAPI()
