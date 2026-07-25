-- 1) Insira 5 usuários
insert into users (first_name, last_name, email, password_hash) values
("João Gabriel", "Mendes", "gaba@email.com", round(rand()  * 100000)),
("Maria Luiza", "Pontes", "lu@email.com", round(rand()  * 100000)),
("Maria Alice", "Pondes", "alice@email.com", round(rand()  * 100000)),
("Gai", "Celestina", "gai@email.com", round(rand()  * 100000)),
("Mãe", "Mendes", "mae@email.com", round(rand()  * 100000))

UPDATE users set salary = round(rand()  * 10000, 2) WHERE id IN 
(212, 213, 214, 215, 216)

-- 2) Insira 5 perfís para os usuários inseridos
-- ALTER TABLE users ADD perfil VARCHAR(150);
INSERT INTO profiles (bio, description, user_id) VALUES
('Uma bio', 'Uma description', (select id from users where email = 'email1@a.com')),
('Uma bio', 'Uma description', (select id from users where email = 'email2@a.com')),
('Uma bio', 'Uma description', (select id from users where email = 'email3@a.com')),
('Uma bio', 'Uma description', (select id from users where email = 'email4@a.com')),
('Uma bio', 'Uma description', (select id from users where email = 'email5@a.com'))

-- 3) Insira permissões (roles) para os usuários inseridos
/*
INSERT INTO users_roles (user_id, role_id)
VALUES
(212, 103), (213, 104), (214, 105), (215, 105), (216, 106)
*/
insert into users_roles (user_id, role_id) values 
(
	(select id from users where email = 'email1@a.com'),
	(select id from roles where name = 'PUT')
),
(
	(select id from users where email = 'email2@a.com'),
	(select id from roles where name = 'PUT')
),
(
	(select id from users where email = 'email3@a.com'),
	(select id from roles where name = 'PUT')
),
(
	(select id from users where email = 'email4@a.com'),
	(select id from roles where name = 'PUT')
),
(
	(select id from users where email = 'email5@a.com'),
	(select id from roles where name = 'PUT')
),
(
	(select id from users where email = 'email5@a.com'),
	(select id from roles where name = 'POST')
),
(
	(select id from users where email = 'email5@a.com'),
	(select id from roles where name = 'GET')
)


-- 4) Selecione os últimos 5 usuários por ordem decrescente
/*
SELECT user_id, role_id from users_roles WHERE
user_id IN (212, 213, 214, 215, 216) and role_id IN (103, 104, 105, 105, 106)

SELECT
FROM users
ORDER BY id DESC
LIMIT 5;
*/
SELECT * FROM users ORDER BY id DESC LIMIT 5;

-- 5) Atualize o último usuário inserido
UPDATE users
SET first_name = "MinhaMãe", last_name = "M Mendes",
WHERE id ORDER BY id DESC LIMIT 1
-- UPDATE users set first_name='Elis Regina', last_name='Atualizada' WHERE id = 624;

-- 6) Remova uma permissão de algum usuário
-- REVOKE DELETE ON users_roles FROM id = 215;
delete 
-- select *
from users_roles where
user_id = (select id from users where email = 'email5@a.com') AND 
role_id = (select id from roles where name='POST')

-- 7) Remova um usuário que tem a permissão "PUT"
-- SELECT u.id as uid, u.first_name, r.name
delete u
from users u
inner join users_roles ur on u.id = ur.user_id 
inner join roles r on ur.role_id = r.id
where r.name  = 'PUT' and u.id = 216

-- 8) Selecione usuários com perfís e permissões (obrigatório)
SELECT u.id as uid, u.first_name, r.name, p.bio 
from users u
inner join users_roles ur on u.id = ur.user_id 
inner join roles r on ur.role_id = r.id
inner join profiles p on p.user_id = u.id;

-- 9) Selecione usuários com perfís e permissões (opcional)
SELECT u.id as uid, u.first_name, r.name, p.bio 
from users u
left join users_roles ur on u.id = ur.user_id 
left join roles r on ur.role_id = r.id
left join profiles p on p.user_id = u.id;

-- 10) Selecione usuários com perfís e permissões ordenando por salário
SELECT u.id as uid, u.first_name, r.name, p.bio, u.salary 
from users u
left join users_roles ur on u.id = ur.user_id 
left join roles r on ur.role_id = r.id
left join profiles p on p.user_id = u.id
order by u.salary ASC;