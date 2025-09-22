-- Problem Link: https://leetcode.com/problems/department-top-three-salaries/description/?envType=study-plan-v2&envId=top-sql-50

select Department, Employee, Salary
from
(select d.name as Department, e.name as Employee, salary as Salary, dense_rank() over(partition by departmentId order by salary desc) as rnk
from Employee e left join Department d 
on e.departmentId=d.id) x
where rnk<=3
