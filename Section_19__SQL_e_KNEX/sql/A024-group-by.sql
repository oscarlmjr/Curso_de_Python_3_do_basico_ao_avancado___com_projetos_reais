-- Group by - Agrupa valores
-- SELECT first_name FROM users
-- SELECT id, first_name FROM users
SELECT first_name, COUNT(id) as total FROM users
GROUP BY first_name
-- ORDER BY first_name ASC;
ORDER BY total DESC;

-- select u.first_name, p.bio from users u
-- select u.first_name from users u
select u.first_name, COUNT(u.id) as total from users u
-- join profiles as p
left join profiles as p
on p.user_id = u.id
-- WHERE u.id = 211
WHERE u.id IN (132, 134, 211, 206)
GROUP BY first_name
ORDER BY total DESC
LIMIT 5;