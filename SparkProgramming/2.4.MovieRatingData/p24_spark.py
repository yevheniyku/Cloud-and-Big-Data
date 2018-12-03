from pyspark import SparkConf, SparkContext

def rating(x):
    if(x <= 1) : return 1
    if(x <= 2) : return 2
    if(x <= 3) : return 3
    if(x <= 4) : return 4
    else : return 5

def movieRating(input):
    ratingsRDD = input.map(lambda x: x.split(","))
    ratingsRDD = ratingsRDD.map(lambda x: (x[1], float(x[2])))
    ratingsRDD = ratingsRDD.groupByKey().sortByKey()
    ratingsRDD = ratingsRDD.map(lambda x: (x[0], sum(list(x[1]))/len(x[1])))
    ratingsRDD = ratingsRDD.map(lambda x: (x[0], rating(float(x[1]))))

    ratingsRDD.sortByKey()
    ratingsRDD.saveAsTextFile("output")

def main():
        conf = SparkConf().setMaster('local').setAppName('MovieRating')
        sc = SparkContext(conf = conf)
        input = sc.textFile("ratings.csv")

        movieRating(input)

if __name__ == '__main__':
    main()
