#!/usr/bin/python

import sys
import re

###################################################################
# Busca las lineas de texto donde aparece la palabra buscada
###################################################################
def mapper(w):
    for line in sys.stdin:
        line = re.sub( r'^\W+|\W+$', '', line )
        words = re.split(r"\W+", line)

        for word in words:
            if w == word:
                print(word.lower() + "\t" + line)

def main():
    w = sys.argv[1]
    mapper(w)

if __name__ == "__main__":
    main()
