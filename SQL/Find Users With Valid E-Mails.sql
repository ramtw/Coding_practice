-- Problem Link: https://leetcode.com/problems/find-users-with-valid-e-mails/?envType=study-plan-v2&envId=top-sql-50
--Write your MySQL query statement below

-- Method-1
select * from Users
where REGEXP_LIKE(mail, '^[a-zA-Z][a-zA-Z0-9_\\-.]*@leetcode\\.com$', 'c')



-- Method-2
select * from Users
where REGEXP_LIKE(mail, '^[a-zA-Z][a-zA-Z0-9_\\-.]*@leetcode[.]com$', 'c')
