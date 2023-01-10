#!/usr/bin/python3
def multiple_returns(sentence):
    sentences = list(sentence)
    new_sentence = []
    if sentences is None or len(sentences) < 1:
        lgth = 0
        index = None
        new_sentence.append(lgth)
        new_sentence.append(index)
        result = tuple(new_sentence)
        return (result)
    else:
        lgth = len(sentences)
        index = sentences[0]
        new_sentence.append(lgth)
        new_sentence.append(index)
        result = tuple(new_sentence)
        return (result)
