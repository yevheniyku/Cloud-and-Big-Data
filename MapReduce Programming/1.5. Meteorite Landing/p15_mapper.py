#!/usr/bin/python

import sys
import re

##################################################################
# parsea el csv sacando los tipos de meteoritos y su masa
##################################################################
def mapper():

    for line in sys.stdin:

        line = re.sub( r'^\W+|\W+$', '', line )
        info = line.split(",")

        meteoriteClass = info[3]
        if(not any(char.isalpha() for char in info[4])):
            meteoriteMass = info[4]
        else:
            meteoriteMass = info[5]

        if(meteoriteMass != ""):
            print (meteoriteClass.lower() + '\t' + str(meteoriteMass))

def main():
    mapper()

if __name__ == "__main__":
    main()
