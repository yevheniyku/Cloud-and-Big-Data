#!/usr/bin/python

import sys

#######################################################
# Analiza los datos recibidos desde el pipe mostrando
# el rango en el que estan las peliculas y sus id
#######################################################
def mapper():
    for line in sys.stdin:
        data = line.split("\t")
        movieId = data[0]
        rating = float(data[1])
        range = ""

        if(rating <= 1):
            range = "Range 1"
        elif(rating <= 2):
            range = "Range 2"
        elif(rating <= 3):
            range = "Range 3"
        elif (rating <= 4):
            range = "Range 4"
        else:
            range = "Range 5"

        print(range + "\t" + str(movieId))

def main():
    mapper()

if __name__ == "__main__":
    main()
