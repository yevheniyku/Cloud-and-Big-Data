#!/usr/bin/python

import sys

##############################################################
# Agrupa los id de las peliculas y calcula las valoraciones
# medias
##############################################################
def reducer():
    previous = None
    sum = 0
    len = 0

    for line in sys.stdin:
        key, value = line.split( '\t' )

        if key != previous:
            if previous is not None:
                print("{}\t{}".format(previous, sum/len))
            previous = key
            sum = 0
            len = 0

        sum = sum + float(value)
        len += 1

    print("{}\t{}".format(previous, (sum/len)))

def main():
    reducer()

if __name__ == "__main__":
    main()
