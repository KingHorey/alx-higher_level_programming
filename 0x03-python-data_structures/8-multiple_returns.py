#!/usr/bin/python3
def multiple_returns(sentence):
    new_sentence = list(sentence)
    if sentence is None:
        lgth = 0
        index = None
        result = tuple(lgth, index)
        return (result)
    else:
        lgth = len(new_sentence)
        index = new_sentence[0]
        result = tuple(lgth, index)
        return (result)
