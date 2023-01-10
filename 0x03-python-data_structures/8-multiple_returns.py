#!/usr/bin/python3
def multiple_returns(sentence):
    new_sentence = []
    if sentence is None:
        lgth = 0
        index = None
        new_sentence.append(lgth)
        new_sentence.append(index)
        result = tuple(new_sentence)
        return (result)
    else:
        lgth = len(sentence)
        index = sentence[0]
        new_sentence.append(lgth)
        new_sentence.append(index)
        result = tuple(new_sentence)
        return (result)
