# #
# # from pyspark import SparkContext, SparkConf
# #
# # conf = SparkConf().setAppName("IPCount").setMaster("local[*]")
# # sc = SparkContext(conf=conf)
# #
# # data=[ "168.182.0.1.1","168.182.0.1.2","168.182.0.1.1","168.182.0.1.3",
# #  "168.182.0.1.2","168.182.0.1.1","168.182.0.1.3","168.182.0.1.4",
# #  "168.182.0.1.3","168.182.0.1.1","168.182.0.1.3","168.182.0.1.2",
# #  "168.182.0.1.4","168.182.0.1.1","168.182.0.1.2","168.182.0.1.1"
# # ]
# #
# # rdd =sc.parallelize(data)
# # print(rdd.collect())
# #
# # pair_rdd=rdd.map(lambda x: (x,1))
# #
# # reduce_key=pair_rdd.reduceByKey(lambda x,y:x+y)
# #
#
# from pyspark import SparkConf, SparkContext
#
# # 1️⃣ Create Spark configuration
# conf = SparkConf() \
#     .setAppName("IPAnalysis") \
#     .setMaster("local[*]")
#
# # 2️⃣ Create SparkContext
# sc = SparkContext(conf=conf)
#
# # 3️⃣ Input data
# data = [
#  "168.182.0.1.1","168.182.0.1.2","168.182.0.1.1","168.182.0.1.3",
#  "168.182.0.1.2","168.182.0.1.1","168.182.0.1.3","168.182.0.1.4",
#  "168.182.0.1.3","168.182.0.1.1","168.182.0.1.3","168.182.0.1.2",
#  "168.182.0.1.4","168.182.0.1.1","168.182.0.1.2","168.182.0.1.1"
# ]
#
# # 4️⃣ Create RDD
# rdd = sc.parallelize(data)
#
# # 5️⃣ Convert to (ip, 1)
# pair_rdd = rdd.map(lambda x: (x, 1))
#
# # 6️⃣ reduceByKey → count frequency
# count_rdd = pair_rdd.reduceByKey(lambda a, b: a + b)
#
# # 7️⃣ sortByKey → sort by IP
# sorted_by_key = count_rdd.sortByKey()
#
# # 8️⃣ sortBy → sort by count descending
# sorted_by_count = count_rdd.sortBy(lambda x: x[1], ascending=False)
#
# # 9️⃣ groupByKey (not recommended but shown)
# grouped = pair_rdd.groupByKey().mapValues(sum)
#
# # 🔟 Second highest IP
# second_highest = sorted_by_count.take(2)[1]
#
# # 🔍 Output
# print("Counts:", count_rdd.collect())
# print("Sorted by count:", sorted_by_count.collect())
# print("Second highest IP:", second_highest)
#
# # 1️⃣1️⃣ Stop Spark
# sc.stop()



from pyspark import SparkContext

sc = SparkContext(master="local[*]", appName="SecondHighestIP")

# Input data
data = [
    "168.182.0.1.1","168.182.0.1.2","168.182.0.1.1","168.182.0.1.3",
    "168.182.0.1.2","168.182.0.1.1","168.182.0.1.3","168.182.0.1.4",
    "168.182.0.1.3","168.182.0.1.1","168.182.0.1.3","168.182.0.1.2",
    "168.182.0.1.4","168.182.0.1.1","168.182.0.1.2","168.182.0.1.1"
]

# Create RDD
rdd = sc.parallelize(data)

# ----------------------------
# 1. map (IP, 1)
# ----------------------------
mapped_rdd = rdd.map(lambda ip: (ip, 1))

# ----------------------------
# 2. reduceByKey (count per IP)
# ----------------------------
count_rdd = mapped_rdd.reduceByKey(lambda a, b: a + b)

# ----------------------------
# 3. groupByKey (for learning purpose)
# ----------------------------
grouped_rdd = mapped_rdd.groupByKey() \
    .mapValues(lambda values: sum(values))

# ----------------------------
# 4. sortByKey (alphabetical IP)
# ----------------------------
sorted_by_key = count_rdd.sortByKey()

# ----------------------------
# 5. sortBy (count descending)
# ----------------------------
sorted_by_count = count_rdd.sortBy(lambda x: x[1], ascending=False)

# ----------------------------
# 6. Find SECOND HIGHEST
# ----------------------------
second_highest = sorted_by_count.take(2)[1]

# ----------------------------
# Print results
# ----------------------------
print("IP Count using reduceByKey:")
print(count_rdd.collect())

print("\nIP Count using groupByKey:")
print(grouped_rdd.collect())

print("\nSorted by IP (sortByKey):")
print(sorted_by_key.collect())

print("\nSorted by Count Desc (sortBy):")
print(sorted_by_count.collect())

print("\nSecond Highest IP:")
print(second_highest)

sc.stop()
