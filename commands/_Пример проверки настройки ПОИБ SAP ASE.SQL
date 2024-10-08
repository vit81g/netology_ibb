-- ����������� � ����:
isql -U<uname> -P<password> -S<SID> -X

-- ������ ��:
use master
go
sp_helpdb
go

-- �������� ��������� ��������:
sp_passwordpolicy list
go

-- �������� ���� �� �������
sp_helpprotect "master.dbo.syslogins"
go

-- �������� ������ ��������������� ��:
sp_locklogin
go

-- �������� ������ ��:
select name, status, dbname from master.dbo.syslogins
go

-- �������� ����������� ������������� �����:
sp_displayroles bondfilv
go

-- �������� ��������� ������ ��������������� ����������:
exec sp_configure 'enable granular permissions'
go

-- �������� �������� ������ ������:
use sybsecurity
go
select count(*) from sysobjects where name like "sysaudits%"
go
select * from sysobjects where name like "sysaudits%"
go

-- �������� ��������� ������:
sp_configure "auditing"
go

-- �������� �������� ������:
sp_displayaudit
go
--
select * from sybsecurity.dbo.sysauditoptions
go

-- �������� �������� �� ���
sp_displaylogin KOLOANDP
go

-- �������� �������� ������� ���
use master
go
sp_securityprofile 'attributes', 'login profile', 'aibprof'
go

-- �������� ������������� � ��������
use master
go
sp_securityprofile 'bindings', 'login profile', 'aibprof'
go

use master
go
sp_securityprofile 'bindings', 'login profile', '%'
go


-- �������� �������
use master
go
sp_securityprofile 'attributes', 'login profile', 'aib_prf'
go


-- �������� ������ �� � ��������� �����
select t1.name, t3.name from syslogins t1, sysloginroles t2, syssrvroles t3 where t2.suid = t1.suid and t3.srid = t2.srid union select name, 'no roles' from syslogins where suid not in (select suid from sysloginroles)
go
Gazprom*123