-- WHERE filtra registros
-- operadores de comparação = < <= > >= <> ou !=
-- operadores lógicos and e or
SELECT * FROM users
-- WHERE id=110;
-- WHERE first_name = "Luiz";
-- WHERE id>100;
-- WHERE id<>110;
WHERE created_at < '2026-07-22 11:12:17'
and first_name = 'Luiz'
-- or first_name = 'Luiz1';
and password_hash = 'a_hash';