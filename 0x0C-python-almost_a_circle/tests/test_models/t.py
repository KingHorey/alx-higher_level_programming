#!/usr/bin/python3

try:
    with open('Rectangles.json') as f:
        content = f.read()
except FileNotFoundError:
    print('file not found')

