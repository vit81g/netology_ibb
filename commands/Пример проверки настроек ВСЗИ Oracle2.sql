-- Просмотр состояния опции ODV
set line 400
set pagesize 2000
col PARAMETER format a25
col VALUE format a10
select PARAMETER, VALUE from V$OPTION where PARAMETER='Oracle Database Vault';

-- Просмотр имени экземпляра
select INSTANCE_NAME from V$INSTANCE;

-- Просмотр текущих сессий
set line 400
set pagesize 2000
col username format a15
col machine format a15
col program format a40
select username, machine, program from v_$session where type != 'BACKGROUND' and program is not null and username='TEST';

-- Просмотр текста функции парольной политики
select TEXT from DBA_SOURCE where NAME='VERIFY_FUNCTION';

-- Просмотр состояния аудита
set line 400
show parameter aud%

-- Просмотр параметров аудита
set line 400
set pagesize 2000
col AUDIT_OPTION format a30
col SUCCESS format a20
col FAILURE format a20
col USER_NAME format a30
-- Все опции со всеми параметрами
select AUDIT_OPTION, SUCCESS, FAILURE, USER_NAME from dba_stmt_audit_opts order by 1;
-- Список включенных опций без вывода параметров
select AUDIT_OPTION from dba_stmt_audit_opts;
-- Список опций без привязки к УЗ
select AUDIT_OPTION from dba_stmt_audit_opts where USER_NAME is NULL order by 1;
-- Список опций, привязанных к УЗ
select AUDIT_OPTION, SUCCESS, FAILURE, USER_NAME from dba_stmt_audit_opts where USER_NAME is not NULL order by 4,1;
-- Определенной опции
select AUDIT_OPTION, SUCCESS, FAILURE, USER_NAME from dba_stmt_audit_opts where AUDIT_OPTION like '%PUBLIC%';

-- Просмотр списка пользователей с паролем по умолчанию
set line 400
set pagesize 2000
col USERNAME format a25
col PRODUCT format a125
select USERNAME, PRODUCT from DBA_USERS_WITH_DEFPWD order by 1;
-- Просмотр активных пользователей с паролем по умолчанию
select U.USERNAME, S.ACCOUNT_STATUS from DBA_USERS_WITH_DEFPWD U, DBA_USERS S where U.USERNAME = S.USERNAME and S.ACCOUNT_STATUS='OPEN' order by 1;

-- Просмотр списка профилей
select distinct PROFILE from DBA_PROFILES order by 1;

-- Просмотр настроек профилей
-- В зависимости от проекта может настраиваться профиль DCMPROF
set line 128
set pagesize 2000
col RESOURCE_NAME format a50
col LIMIT format a30
select RESOURCE_NAME, LIMIT from DBA_PROFILES where profile='SYSPROF';
select RESOURCE_NAME, LIMIT from DBA_PROFILES where profile='DEFAULT';
select RESOURCE_NAME, LIMIT from DBA_PROFILES where profile='SAPUPROF';
select RESOURCE_NAME, LIMIT from DBA_PROFILES where profile='SERVPROF';
select RESOURCE_NAME, LIMIT from DBA_PROFILES where profile='DCMPROF';
select RESOURCE_NAME, LIMIT from DBA_PROFILES where profile='SAPPROF';
select RESOURCE_NAME, LIMIT from DBA_PROFILES where profile='FINDER_PROF';
select RESOURCE_NAME, LIMIT from DBA_PROFILES where profile='MONITORING_PROFILE';

-- Просмотр настроек пользователей (назначенный профиль, статус аккаунта)
set line 400
set pagesize 2000
col USERNAME format a25
col PROFILE format a20
col ACCOUNT_STATUS format a16
select USERNAME, PROFILE, ACCOUNT_STATUS from DBA_USERS order by 1;
-- Просмотр настроек активных пользователей
select USERNAME, PROFILE, ACCOUNT_STATUS from DBA_USERS where ACCOUNT_STATUS='OPEN' order by 1;
-- Просмотр настроек определенного пользователя
select USERNAME, PROFILE, ACCOUNT_STATUS from DBA_USERS where USERNAME='SYSTEM';
select USERNAME, PROFILE, ACCOUNT_STATUS from DBA_USERS where username='IDMUSER';
select USERNAME, PROFILE, ACCOUNT_STATUS from DBA_USERS where USERNAME like '%SAPSR%';
select USERNAME, PROFILE, ACCOUNT_STATUS from DBA_USERS where USERNAME='ORABACKUP';
-- Просмотр списка пользователей с определенным профилем
select USERNAME, ACCOUNT_STATUS from DBA_USERS where profile='DEFAULT' order by 1;
select USERNAME, ACCOUNT_STATUS from DBA_USERS where profile='SAPPROF' order by 1;
select USERNAME, ACCOUNT_STATUS from DBA_USERS where profile='SAPUPROF' order by 1;
select USERNAME, ACCOUNT_STATUS from DBA_USERS where profile='SYSPROF' order by 1;
select USERNAME, ACCOUNT_STATUS from DBA_USERS where profile='FINDER_PROF' order by 1;
-- Просмотр данных по блокировке пользователей
select USERNAME, ACCOUNT_STATUS, EXPIRY_DATE, LOCK_DATE, LAST_LOGIN from DBA_USERS where profile='SYSPROF' order by 1;
-- Просмотр данных по блокировке пользователей (для версии 11)
select USERNAME, ACCOUNT_STATUS, EXPIRY_DATE, LOCK_DATE from DBA_USERS where profile='SYSPROF' order by 1;

-- Просмотр списка ролей
select ROLE from DBA_ROLES order by 1;
select ROLE from DBA_ROLES where ROLE in ('MPSAPJAVAROLE', 'MPROLE');

-- Просмотр списка пользователей с назначенной ролью
set line 400
set pagesize 2000
col GRANTEE format a25
col GRANTED_ROLE format a15
col ADMIN_OPTION format a12
select GRANTEE, GRANTED_ROLE, ADMIN_OPTION  from DBA_ROLE_PRIVS where GRANTED_ROLE='AIBROLE' order by 1;
select GRANTEE, GRANTED_ROLE, ADMIN_OPTION  from DBA_ROLE_PRIVS where GRANTED_ROLE='MPROLE' order by 1;
select GRANTEE, GRANTED_ROLE, ADMIN_OPTION  from DBA_ROLE_PRIVS where GRANTED_ROLE='DV_SECANALYST' order by 1;
select GRANTEE, GRANTED_ROLE, ADMIN_OPTION  from DBA_ROLE_PRIVS where GRANTED_ROLE='DV_ACCTMGR' order by 1;
select GRANTEE, GRANTED_ROLE, ADMIN_OPTION  from DBA_ROLE_PRIVS where GRANTED_ROLE='CONNECT' order by 1;

-- Просмотр списка ролей, назначенных пользователю
set line 400
set pagesize 2000
col GRANTEE format a25
col GRANTED_ROLE format a15
select GRANTEE,GRANTED_ROLE from DBA_ROLE_PRIVS where GRANTEE='IDMUSER';
select GRANTEE,GRANTED_ROLE from DBA_ROLE_PRIVS where GRANTEE='AIBROLE';
select GRANTEE,GRANTED_ROLE from DBA_ROLE_PRIVS where GRANTEE='BRTDBA';
select GRANTEE,GRANTED_ROLE from DBA_ROLE_PRIVS where GRANTEE='SECMGRPRIVS_ROLE';
select GRANTEE,GRANTED_ROLE from DBA_ROLE_PRIVS where GRANTEE='OPS$ORAH1B';
select GRANTEE,GRANTED_ROLE from DBA_ROLE_PRIVS where GRANTEE='MPSAPJ';
select GRANTEE,GRANTED_ROLE from DBA_ROLE_PRIVS where GRANTEE='SAPACCTMGR';
select GRANTEE,GRANTED_ROLE from DBA_ROLE_PRIVS where GRANTEE='MPROLE';
select GRANTEE,GRANTED_ROLE from DBA_ROLE_PRIVS where GRANTEE='SECACCTMGR';

-- Просмотр прав на таблицы
set line 400
set pagesize 2000
col OWNER format a15
col TABLE_NAME format a45
col PRIVILEGE format a15
col GRANTEE format a15
select OWNER, TABLE_NAME, PRIVILEGE, GRANTEE from DBA_TAB_PRIVS where GRANTEE='AIBROLE' order by 1,2;
select OWNER, TABLE_NAME, PRIVILEGE, GRANTEE from DBA_TAB_PRIVS where GRANTEE='IDMUSER' order by 1,2;
select OWNER, TABLE_NAME, PRIVILEGE, GRANTEE from DBA_TAB_PRIVS where GRANTEE='MPROLE' order by 1,2;
select OWNER, TABLE_NAME, PRIVILEGE, GRANTEE from DBA_TAB_PRIVS where GRANTEE='OPS$ORAH1B'by 1,2;

-- Просмотр системных привилегий
set line 400
set pagesize 2000
col PRIVILEGE format a30
col GRANTEE format a15
select PRIVILEGE, GRANTEE from DBA_SYS_PRIVS where GRANTEE='MPROLE' order by 1;
select PRIVILEGE, GRANTEE from DBA_SYS_PRIVS where GRANTEE='AIBROLE' order by 1;
select PRIVILEGE, GRANTEE from DBA_SYS_PRIVS where GRANTEE='DV_SECANALYST' order by 1;
select PRIVILEGE, GRANTEE from DBA_SYS_PRIVS where GRANTEE='ORABACKUP' order by 1;
select PRIVILEGE, GRANTEE from DBA_SYS_PRIVS where GRANTEE='IDMUSER' order by 1;

-- Просмотр зарегистрированных триггеров
set linesize 400
set pagesize 2000
col TRIGGER_NAME a15
col BASE_OBJECT_TYPE format a8
col TRIGGER_TYPE format a20
col TRIGGERING_EVENT format a15
col STATUS format a10
col DESCRIPTION format a40
select TRIGGER_NAME,BASE_OBJECT_TYPE,TRIGGER_TYPE,TRIGGERING_EVENT,STATUS, DESCRIPTION from all_triggers where OWNER='IDMUSER';

-- Просмотр тела триггера
set line 400
set pagesize 2000
set LONG 1000
select TRIGGER_BODY from ALL_TRIGGERS where TRIGGER_NAME='ATR_LOGON';

-- Поиск хранимой процедуры
set line 400
set pagesize 2000
select distinct NAME from ALL_SOURCE where TYPE='PROCEDURE' and OWNER='IDMUSER';

-- Просмотр текста хранимой процедуры
set line 400
set pagesize 2000
set LONG 1000
select TEXT from ALL_SOURCE where NAME='UPR_USER_LOGON_DELETE';

-- Просмотр статуса и настройки задач планировщика
set line 400
set pagesize 2000
col OWNER format a5
col JOB_NAME format a22
col ENABLED format a6
col JOB_ACTION format a80
col RUN_COUNT format a2
col LAST_START_DATE format a15
col NEXT_RUN_DATE format a15
select OWNER, JOB_NAME, ENABLED, JOB_ACTION, LAST_START_DATE,NEXT_RUN_DATE from DBA_SCHEDULER_JOBS where JOB_NAME like '%TRAIL%';
