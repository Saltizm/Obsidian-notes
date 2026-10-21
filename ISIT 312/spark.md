---
index: true
course: "ISIT 312"
chapter: "Big data platforms"
concept: "spark"
---

# spark

.map() - java datastream. returns array with before and after operation (split by line) 
.flatmap() - java datastream. return array with before and after operation (all in one)
.reduce() - conditional stream
.count() - get number of rows
.show() - display in table format
	show(number, truncate=true)
groupByKey() - group arrays of identical keys
.collect() - convert dataframe into array

.filter()

trim - remove whitespace
toInt - atoi

spark.sparkContext - same as .sc creates rdd
spark.read.textFile - read textfile 

.createOrReplaceTempView("name")

rdd -> df(hadoop table) <>ds(oop)