-- Problem Link: https://leetcode.com/problems/second-highest-salary/description/?envType=study-plan-v2&envId=top-sql-50
-- Method: 1
(select distinct salary SecondHighestSalary
from Employee
order by 1 desc
limit 1 offset 1)
union all
select null as SecondHighestSalary
limit 1;

-- Method: 2
--scalar sub query: return single value, handles null
select
(select distinct Salary 
from Employee order by salary desc 
limit 1 offset 1) 
as SecondHighestSalary;
