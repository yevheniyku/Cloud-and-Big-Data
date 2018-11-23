#!/usr/bin/python

import sys
import re

##########################################################
# Parsea los datos y saca los id de las peliculas y sus
# valoraciones
##########################################################
def mapper():
    for line in sys.stdin:
        line = re.sub( r'^\W+|\W+$', '', line )
        data = line.split(",")

        movieId = data[1]
        rating = data[2]

        print("{}\t{}".format(movieId, rating))

def main():
    mapper()

if __name__ == "__main__":
    main()
