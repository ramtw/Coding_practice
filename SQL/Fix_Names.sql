-- Problem Link: https://leetcode.com/problems/fix-names-in-a-table/?envType=study-plan-v2&envId=top-sql-50

select user_id, concat(upper(substring(name, 1, 1)), lower(substring(name, 2))) as name
from users
