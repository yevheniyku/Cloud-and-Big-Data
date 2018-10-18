#!/usr/bin/python

import sys

previous = ""
sum = ""

for line in sys.stdin:
    key, value = line.split( '\t' )
    sum = sum + '\t' + value

print(key + sum)
