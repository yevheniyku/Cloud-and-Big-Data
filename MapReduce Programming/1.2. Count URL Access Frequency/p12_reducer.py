#!/usr/bin/python

import sys

###########################################################
# Recibe la entrada por stdin y calcula el numero de veces
# que una url ha sido accedida
###########################################################
def reducer():
    previous = None
    sum = 0

    for line in sys.stdin:
        key, value = line.split( '\t' )

        if key != previous:
            if previous is not None:
                print('{}\t{}'.format(sum, previous))
            previous = key
            sum = 0

        sum = sum + int( value )

    print('{}\t{}'.format(sum, previous))

def main():
    reducer()

if __name__ == "__main__":
    main()
