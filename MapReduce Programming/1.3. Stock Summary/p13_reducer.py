#!/usr/bin/python

import sys

previous = None
sum = 0
length = 1

for line in sys.stdin:
    key, value = line.split('\t')

    if key != previous:
        if previous is not None:
            print previous + "\t" + str(sum/length)
        previous = key
        sum = 0
        length = 1

    sum = sum + float(value)
    length += 1

print previous + '\t' + str(sum/length)
