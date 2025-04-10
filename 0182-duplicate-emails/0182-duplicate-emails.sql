# Write your MySQL query statement below
select email from Person group by 1 HAVING count(email)>1 ;
