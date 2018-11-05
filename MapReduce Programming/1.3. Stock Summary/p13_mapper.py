#!/usr/bin/python

import sys
import re

firstline = True

for line in sys.stdin:

    line = re.sub( r'^\W+|\W+$', '', line )

    # Another way to check the first firstline
    #if(not any(char.isalpha() for char in line))

    # Checks if it is the first line of input that contains
    # the column names
    if(firstline):
        firstline = False
    else:
        info = line.split(",")

        # Getting the year
        date = info[0]
        yearToSplit = date.split("-")
        year = yearToSplit[0]

        # Price at close
        price = info[4]

        print(year + "\t" + price)
