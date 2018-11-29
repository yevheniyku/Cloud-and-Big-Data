from pyspark import SparkConf, SparkContext

#############################################################################
# Coge el log de acceso a las url y calcula el numero de veces que ha sido
# visitada cada URL
#############################################################################
def urlCounter(input):
    rddsplit = input.map(lambda x: x.split())
    urlList = rddsplit.map(lambda x: x[0])
    urlListCount = urlList.map(lambda x: (x, 1))
    urlVisits = urlListCount.reduceByKey(lambda x,y: x+y)

    urlVisits.saveAsTextFile("output.txt")

def main():
    conf = SparkConf().setMaster('local').setAppName('DistributedGrep')
    sc = SparkContext(conf = conf)
    input = sc.textFile("access_log")

    urlCounter(input)

if __name__ == '__main__':
    main()
