/* Write your PL/SQL query statement below */
select author_id  "id"
from Views 
where viewer_id = author_id 
group by author_id
having count(*)>=1
order by author_id ;