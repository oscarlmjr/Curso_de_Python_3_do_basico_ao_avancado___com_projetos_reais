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
ALTER TABLE users ADD perfil VARCHAR(150);

-- 3) Insira permissões (roles) para os usuários inseridos

INSERT INTO users_roles (user_id, role_id)
VALUES
(212, 103), (213, 104), (214, 105), (215, 105), (216, 106)

-- 4) Selecione os últimos 5 usuários por ordem decrescente
SELECT user_id, role_id from users_roles WHERE
user_id IN (212, 213, 214, 215, 216) and role_id IN (103, 104, 105, 105, 106)

SELECT
FROM users
ORDER BY id DESC
LIMIT 5;

-- 5) Atualize o último usuário inserido
UPDATE users
SET first_name = "MinhaMãe", last_name = "M Mendes",
WHERE id ORDER BY id DESC LIMIT 1

-- 6) Remova uma permissão de algum usuário
REVOKE DELETE ON users_roles FROM id = 215;