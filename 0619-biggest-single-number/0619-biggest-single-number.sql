/* Write your PL/SQL query statement below */
select MAX(num) "num"
from MYNumbers
where num in (select num 
from MYNumbers
group by num 
having count(*) = 1);