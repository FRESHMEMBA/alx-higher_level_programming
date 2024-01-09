#!/usr/bin/python3
def multiple_returns(sentence):
    return (len(sentence), None if len(senctence) == 0 else sentence[0])
