#!/usr/bin/python

import sys

##############################################################
# Agrupa los rangos de las peliculas y sus id
##############################################################
def reducer():
    previous = None
    sum = ""

    for line in sys.stdin:
        key, value = line.split( '\t' )

        if key != previous:
            if previous is not None:
                print("########################################")
                print("\t\t" + previous)
                print("########################################")
                print("\t" + sum)
            previous = key
            sum = ""

        sum = sum + "\t" + str(value)

    print("########################################")
    print("\t\t" + previous)
    print("########################################")
    print(sum)

def main():
    reducer()

if __name__ == "__main__":
    main()
