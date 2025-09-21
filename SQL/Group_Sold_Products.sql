-- Problem Link: https://leetcode.com/problems/group-sold-products-by-the-date/?envType=study-plan-v2&envId=top-sql-50
-- Write your PostgreSQL query statement below
select sell_date, count(distinct product) as num_sold, ARRAY_TO_STRING(array_agg(distinct product order by product), ',') as products
from Activities
group by 1
order by 1;
