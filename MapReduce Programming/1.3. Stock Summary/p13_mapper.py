#!/usr/bin/python

import sys
import re

########################################################
# Lee la entrada por stdin y saca el año y el precio
########################################################
def mapper():
    for line in sys.stdin:

        line = re.sub( r'^\W+|\W+$', '', line )

        info = line.split(",")

        # Getting the year
        date = info[0]
        yearToSplit = date.split("-")
        year = yearToSplit[0]

        # Price at close
        price = info[4]

        print(year + "\t" + price)

def main():
    mapper()

if __name__ == "__main__":
    main()
