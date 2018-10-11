#!/usr/bin/python

import sys
import re

print('What word are you looking for?')
word = input();

print('Where do you want me to look it for you?')
print('(please include the file path and extension)')
fileInput = input()
file = open(fileInput, "r")

#lineNumber is used for showing the line number
lineNumber = 1

for line in file:
    #parsing lines and words
    parsedLine = re.sub(r'^\W+|\W+$', '', line)
    words = re.split(r"\W+", parsedLine)

    #wordsInLine is used for prevention of duplicated lines
    wordsInLine = 0

    for w in words:
        if w == word:
            if wordsInLine == 0:
                wordsInLine += 1
                print("Line {0}: {1}".format(lineNumber, line))
    lineNumber += 1

file.close()
