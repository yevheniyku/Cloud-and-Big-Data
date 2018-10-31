#!/usr/bin/python

import sys
import re

w = sys.argv[1]

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(r"\W+", line)

    for word in words:
        if w == word:
            print(word.lower() + "\t" + line)
