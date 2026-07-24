-- SELECT id FROM users;
-- SELECT MAX(salary) FROM users;
SELECT
max(salary) as max_salary,
min(salary) as min_salary,
avg(salary) as avg_salary,
sum(salary) as sum_salary,
count(salary) as count_salary
FROM users
-- where first_name = 'Carly';

select
-- u.id,
u.first_name,
max(salary) as max_salary,
min(salary) as min_salary,
avg(salary) as avg_salary,
sum(salary) as sum_salary,
COUNT(u.id) as total
from users u
left join profiles as p
on p.user_id = u.id
-- WHERE u.id IN (132, 134, 211, 206)
GROUP BY first_name
-- GROUP BY u.first_name, id
ORDER BY total DESC;