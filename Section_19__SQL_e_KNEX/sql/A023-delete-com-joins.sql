-- Apaga registros com joins
select u.first_name, p.bio from users u
-- join profiles as p
left join profiles as p
on p.user_id = u.id
where u.first_name = 'Katelyn';

-- delete p from users u
delete p, u from users u
-- join profiles as p
left join profiles as p
on p.user_id = u.id
where u.first_name = 'Katelyn';