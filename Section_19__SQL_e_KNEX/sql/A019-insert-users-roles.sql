INSERT INTO users_roles (user_id, role_id)
-- INSERT INTO users_roles (user_id)
VALUES
(122, 104);
-- (122);

SELECT user_id, role_id  from users_roles WHERE
user_id = 122 and role_id = 104;

-- select id, (select 1) as qualquer from users;
-- select 1;
select
id, 
-- (select id from roles) as qualquer 
-- (select id from roles limit 1) as qualquer 
(select id from roles order by rand() limit 1) as qualquer 
from users;

insert into users_roles (user_id, role_id)
select 
id, 
(select id from roles order by rand() limit 1) as qualquer 
from users;
