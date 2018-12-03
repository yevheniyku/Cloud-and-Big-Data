from pyspark import SparkConf, SparkContext

############################################################################
# Busca las lineas que contienen la palabra "soil"
############################################################################
def grep(input, w):
    linesWithWord = input.filter(lambda line: w in line)
    linesWithWord.saveAsTextFile("output.txt")

def main():
    w = "soil"

    conf = SparkConf().setMaster('local').setAppName('DistributedGrep')
    sc = SparkContext(conf = conf)
    input = sc.textFile("input.txt")

    grep(input, w)

if __name__ == '__main__':
    main()
