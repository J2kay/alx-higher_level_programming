#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return None
    length = len(sentence)
    if length > 0:
        return length, sentence[0]
    else:
        return length, None
