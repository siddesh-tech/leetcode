# Write your MySQL query statement below
select name "Customers"
from customers left join orders
on customers.id = orders.customerId
where customerId is null ;