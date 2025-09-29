# Problem Link: https://leetcode.com/problems/second-highest-salary/description/

from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, LongType

data = [[1, 100], [2, 200], [3, 300], [4, 300], [5, 400], [6, 500], [7, 500], [8, 600], [9, 700]]
data1 = [[1, 100], [2, 100], [3, 100]] # no second highest salary


schema = StructType([
    StructField("id", LongType(), True),  
    StructField("salary", LongType(), True) 
])

employee_df = spark.createDataFrame(data, schema=schema)
employee_df.show()

second_highest_salary_df = (
    employee_df
    .select("salary")
    .distinct()
    .orderBy(F.col("salary").desc())
    .limit(2)
)

second_highest_salary = (
    second_highest_salary_df
    .agg(F.collect_list("salary").alias("salaries"))
    .select(
        F.when(
            F.size("salaries") >= 2,
            F.element_at("salaries", 2)
        ).alias("second_highest_salary")
    )
)

# display(second_highest_salary)
second_highest_salary.show()
