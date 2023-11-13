-- Подключение к СУБД:
isql -U<uname> -P<password> -S<SID> -X

-- Список БД:
use master
go
sp_helpdb
go

-- Просмотр парольной политики:
sp_passwordpolicy list
go

-- Просмотр прав на таблицу
sp_helpprotect "master.dbo.syslogins"
go

-- Просмотр списка заблокированных УЗ:
sp_locklogin
go

-- Просмотр списка УЗ:
select name, status, dbname from master.dbo.syslogins
go

-- Просмотр назначенных пользователям ролей:
sp_displayroles bondfilv
go

-- Проверка состояния режима гранулированных привилегий:
exec sp_configure 'enable granular permissions'
go

-- Проверка настроек таблиц аудита:
use sybsecurity
go
select count(*) from sysobjects where name like "sysaudits%"
go
select * from sysobjects where name like "sysaudits%"
go

-- Проверка состояния аудита:
sp_configure "auditing"
go

-- Проверка настроек аудита:
sp_displayaudit
go
--
select * from sybsecurity.dbo.sysauditoptions
go

-- Просмотр настроек УЗ АИБ
sp_displaylogin KOLOANDP
go

-- Просмотр настроек профиля АИБ
use master
go
sp_securityprofile 'attributes', 'login profile', 'aibprof'
go

-- Просмотр пользователей с профилем
use master
go
sp_securityprofile 'bindings', 'login profile', 'aibprof'
go

use master
go
sp_securityprofile 'bindings', 'login profile', '%'
go


-- Просмотр профиля
use master
go
sp_securityprofile 'attributes', 'login profile', 'aib_prf'
go


-- Просмотр списка УЗ с привязкой ролей
select t1.name, t3.name from syslogins t1, sysloginroles t2, syssrvroles t3 where t2.suid = t1.suid and t3.srid = t2.srid union select name, 'no roles' from syslogins where suid not in (select suid from sysloginroles)
go
Gazprom*123