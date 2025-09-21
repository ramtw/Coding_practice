-- Problem Link: https://leetcode.com/problems/list-the-products-ordered-in-a-period/?envType=study-plan-v2&envId=top-sql-50
-- Write your PostgreSQL query statement below

select product_name, sum(unit) as unit
from Orders left join Products using(product_id)
where DATE_TRUNC('month', order_date)='2020-02-01'
group by product_id, product_name
having sum(unit)>=100;
