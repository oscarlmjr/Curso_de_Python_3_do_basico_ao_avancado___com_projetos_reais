-- insert select
-- insere valores em uma tabela usando outra
-- select 1 as coluna;
-- select 1 as coluna, 'qualquer coisa' as col2;
insert into profiles
(bio, description, user_id)
-- SELECT 1,2,110;
-- select 'bio', 'description', id from
-- select first_name, first_name, id
select
concat('Bio de ', first_name), 
concat('Description de', ' ', first_name), id 
from users;




delete from profiles;