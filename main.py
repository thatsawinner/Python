from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("SparkPythonStarter").getOrCreate()

# lines = spark.read.option("inferSchema", True).option("header", True).csv("file:///tmp/people.txt")
lines = spark.read.json("file:///Users/Owner.000/Documents/Ryan/Spark/SparkPythonStarter-master/data/population_data.json")
lines.printSchema()

#doubledAges = lines.select(col("name"), col("age")*2, col("dept"))
#doubledAges.foreach(print)

#averageAgeByDept = lines.groupBy(col("dept")).avg("age")
#averageAgeByDept.foreach(print)


