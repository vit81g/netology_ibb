-- Вывод ролей в PostgreSQL
\du
-- Объектные привилегии в PostgreSQL
\dp
\ddp
\dn+
select * from information_schema.role_table_grants;
--Кто и к какой базе подключен в PostgreSQL
\с 