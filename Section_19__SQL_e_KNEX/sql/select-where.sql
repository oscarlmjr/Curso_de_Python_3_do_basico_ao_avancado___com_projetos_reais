-- BETWEEN seleciona um range
SELECT * FROM users
WHERE 
-- created_at <= '2026-07-22 11:02:06'
-- created_at <= '2026-07-22 11:02:06'
created_at BETWEEN
-- '2026-07-22 00:00:00'
'2021-10-11 23:59:59'
-- created_at >= '2021-10-11 14:19:33';
-- and '2021-10-11 23:59:59'
and '2026-07-22 00:00:00'
and id BETWEEN 125 and 184;