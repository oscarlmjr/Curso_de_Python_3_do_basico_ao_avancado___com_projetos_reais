-- limit limita a qtd de valores
-- offset desloca o cursor para exibir os resultados
SELECT id, first_name, email as uemail 
FROM users
WHERE id BETWEEN 100 and 150
-- ORDER BY first_name  desc
ORDER BY id asc
-- LIMIT 5;
-- LIMIT 2 offset 0;
-- LIMIT 2 offset 2;
-- LIMIT 2 offset 4;
-- LIMIT 3 offset 0;
-- LIMIT 3 offset 3;
-- LIMIT 3 offset 6;
-- LIMIT 3,6;
-- LIMIT 0,3;
-- LIMIT 3,3;
-- LIMIT 6,3;
LIMIT 9,3;