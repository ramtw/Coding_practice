# Problem Link: https://leetcode.com/problems/second-highest-salary/description/

from pyspark.sql import functions as F

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
