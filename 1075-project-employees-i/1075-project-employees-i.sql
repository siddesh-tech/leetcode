/* Write your PL/SQL query statement below */
select project_id , ROUND(avg(experience_years),2 )"average_years"
from project , Employee
where project.employee_id = Employee.employee_id
group by project_id 
order by project_id ;