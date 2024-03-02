#!/usr/bin/python3

""" import requests and sys module """

import requests
import sys


def getCommits():
    """ gets commits from GitHub and list from newest to oldest """
    repo = sys.argv[1]
    name = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(name, repo)

    response = requests.get(url, params={'per_page': 10})
    commits = response.json()

    for commit in commits:
        print(commit.get('sha'), end=": ")
        print(commit.get('commit').get('author').get('name'))


if __name__ == "__main__":
    getCommits()
