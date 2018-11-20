 #!/usr/bin/python

import sys
import re

#######################################################
# Parsea las lineas sacando las URL y poniendo un 1
#######################################################
def mapper():
    for line in sys.stdin:
        line = re.sub( r'^\W+|\W+$', '', line )
        part = line.split(" ")

        print( part[0] + "\t1" )

def main():
    mapper()

if __name__ == "__main__":
    main()
