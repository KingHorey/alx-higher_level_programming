#!/usr/bin/python3

""" No modules imported """


def text_indentation(text):
    """Function prints a text with two new lines
    after either '.', '?' and ':'
    """
    if not isinstance(text, str) or len(text) <= 0:
        raise TypeError("text must be a string")
    words = "".join([x if x not in "?:." else x + "\n" * 2 for x in text])
    words = words.split("\n")

    lgth = len(words)
    i = 0
    while i in range(lgth - 1):
        print(words[i].strip())
        i += 1
    print(words[i].strip(), end="")
