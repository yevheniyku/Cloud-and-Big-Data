#!/usr/bin/python

import sys

##########################################################
# funcion reducer agrupa los meteoritos por su clase
# y saca la masa media de cada clase
##########################################################
def reducer():
    previous = None
    sum = 0
    length = 1

    for line in sys.stdin:
        key, value = line.split( '\t' )

        if key != previous:
            if previous is not None:
                print("{}\t{}".format(previous, (sum/length)))
            previous = key
            sum = 0
            length = 1

        sum = sum + float( value )
        length += 1

    print("{}\t{}".format(previous, sum/length))

def main():
    reducer()

if __name__ == "__main__":
    main()
