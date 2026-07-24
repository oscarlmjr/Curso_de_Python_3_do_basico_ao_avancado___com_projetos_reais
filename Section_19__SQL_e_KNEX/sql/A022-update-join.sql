-- Atualiza registros com joins
-- select u.first_name from users u 
select u.first_name, p.bio from users u
-- update users as u
join profiles p
on p.user_id = u.id
-- set p.bio =  CONCAT(p.bio, ' atualizado') 
where u.first_name = 'Katelyn';

update users as u
join profiles p
on p.user_id = u.id
set p.bio =  CONCAT(p.bio, ' atualizado') 
where u.first_name = 'Katelyn';