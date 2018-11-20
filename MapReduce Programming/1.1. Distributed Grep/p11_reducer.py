#!/usr/bin/python

import sys

#######################################################
# Agrupa las líneas que le llegan por stdin
#######################################################
def reducer():
    previous = ""
    sum = ""

    for line in sys.stdin:
        key, value = line.split( '\t' )
        sum = sum + '\t' + value

    print(key + sum)

def main():
    reducer()

if __name__ == "__main__":
    main()
