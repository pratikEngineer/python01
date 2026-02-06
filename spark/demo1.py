# from pyspark.sql import SparkSession
#
# spark = SparkSession.builder \
#     .appName("DemoApp") \
#     .master("local[*]") \
#     .getOrCreate()
#
# sc = spark.sparkContext
#
# print(sc.parallelize([1, 2, 3, 4]).collect())
#
# spark.stop()




from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("DemoApp") \
    .master("local[*]") \
    .getOrCreate()

print("Spark started successfully")

spark.stop()
