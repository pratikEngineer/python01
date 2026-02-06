from pyspark import SparkContext

sc = SparkContext(master="local[*]", appName="WordCount")

# Input data
data = [
    "hello spark",
    "hello pyspark",
    "spark with python",
    "hello spark"
    "Hey There"
]

# Create RDD
rdd = sc.parallelize(data)

# Word count logic
word_count = (
    rdd
    .flatMap(lambda line: line.split(" "))
    .map(lambda word: (word, 1))
    .reduceByKey(lambda a, b: a + b)
)

# Print output
print(word_count.collect())

sc.stop()


