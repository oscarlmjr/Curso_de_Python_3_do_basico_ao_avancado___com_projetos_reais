-- Seleciona colunas
SELECT * FROM users;
-- Seleciona coluna email
-- SELECT email FROM users u;
-- SELECT email, id, first_name FROM users u;
SELECT
-- email as e, id as i, first_name as fn
-- email e, id i, first_name "eu posso colocar isso"
-- u.email e, u.id i, u.first_name
u.email uemail, u.id uid, u.first_name ufirst_name
-- FROM users u;
FROM users as u;
