#!/usr/bin/python

import sys

previous = None
sum = 0
len = 1

for line in sys.stdin:
    key, value = line.split( '\t' )

    if key != previous:
        if previous is not None:
            print(previous + '\t' + str( sum/len ))
        previous = key
        sum = 0
        len = 1

    sum = sum + float( value )
    len += 1

print  (previous + '\t' + str( sum/len ))
