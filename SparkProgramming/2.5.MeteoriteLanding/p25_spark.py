from pyspark import SparkConf, SparkContext
import string

################################################################################
# Ya que el archivo no viene bien parseado (algunos valores son nulos)
# se coge el archivo Meteorite_Landings, se limpia y los datos
# necesarios se guardan en un archivo nuevo. Este archivo nuevo
# es con el que vamos a trabajar con Spark
################################################################################
def parseFile(file):
    with open(file, 'r') as f:
        with open('meteorite.csv', 'w') as w:
            for line in f:
                data = line.split(',')
                if(data[4] != ''):
                    if(not any(char.isalpha() for char in data[4])):
                        w.write(data[3] + '\t' + data[4] + '\n')
                    else:
                        if(data[5] != ''):
                            w.write(data[3] + '\t' + data[5] + '\n')

def meteorite(input):
    meteoriteRDD = input.map(lambda x: x.split('\t'))
    meteoriteRDD = meteoriteRDD.map(lambda x: (x[0], float(x[1])))
    meteoriteRDD = meteoriteRDD.groupByKey().sortByKey()
    meteoriteRDD = meteoriteRDD.map(lambda x: (x[0], sum(list(x[1]))/len(x[1])))
    meteoriteRDD = meteoriteRDD.map(lambda x: (x[0], float(x[1])))

    meteoriteRDD.saveAsTextFile('output')

def main():
    parseFile('Meteorite_Landings.csv')

    conf = SparkConf().setMaster('local').setAppName('MeteoriteLanding')
    sc = SparkContext(conf = conf)
    input = sc.textFile('meteorite.csv')

    meteorite(input)


if __name__ == '__main__':
    main()
