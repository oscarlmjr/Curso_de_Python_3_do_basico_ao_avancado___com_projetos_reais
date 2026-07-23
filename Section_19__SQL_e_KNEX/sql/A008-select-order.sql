-- Order ordena valores:
-- order by id asc (id crescente)
-- order by id desc (id decrescente)
-- order by id asc, first_name desc (prioriza o id)
SELECT id, first_name, email as uemail
-- SELECT first_name, email as uemail
FROM users
WHERE id BETWEEN 100 and 150
-- ORDER BY created_at ASC;
-- ORDER BY id ASC;
-- ORDER BY first_name DESC, id ASC;
ORDER BY first_name DESC;