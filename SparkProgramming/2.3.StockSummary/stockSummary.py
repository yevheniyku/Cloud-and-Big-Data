from pyspark import SparkConf, SparkContext

################################################################################
#   Stock counter calcula la media de precios por cada anyo
#   se podria hacerlo con data frames (mas facil) pero me di cuenta tarde
################################################################################
def stockCounter(input):
    tuple = (0,0)
    rddParsed = input.map(lambda x: x.split(','))
    yearStock = rddParsed.map(lambda x: (x[0].split('-')[0], float(x[5])))
    rddAverage = yearStock.aggregateByKey(tuple, lambda a, b: (a[0] + b, a[1] + 1),
                                                 lambda a, b: (a[0] + b[0], a[1] + b[1]))
    finalResult = rddAverage.mapValues(lambda v: v[0]/v[1])
    finalResult.sortByKey().saveAsTextFile("output.txt")

def main():
    conf = SparkConf().setMaster('local').setAppName('DistributedGrep')
    sc = SparkContext(conf = conf)
    input = sc.textFile("GOOGLE.csv")

    stockCounter(input)

if __name__ == '__main__':
    main()
