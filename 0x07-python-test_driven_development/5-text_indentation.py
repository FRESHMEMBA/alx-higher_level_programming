#!/usr/bin/python3
"""
"""

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for c in text:
        print(c, end='' if c not in ".?:" else "\n\n")