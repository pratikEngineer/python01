
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("IPCount").setMaster("local[*]")
sc = SparkContext(conf=conf)

data=[ "168.182.0.1.1","168.182.0.1.2","168.182.0.1.1","168.182.0.1.3",
 "168.182.0.1.2","168.182.0.1.1","168.182.0.1.3","168.182.0.1.4",
 "168.182.0.1.3","168.182.0.1.1","168.182.0.1.3","168.182.0.1.2",
 "168.182.0.1.4","168.182.0.1.1","168.182.0.1.2","168.182.0.1.1"
]

rdd =sc.parallelize(data)
print(rdd.collect())

pair_rdd=rdd.map(lambda x: (x,1))

reduce_key=pair_rdd.reduceByKey(lambda x,y:x+y)

