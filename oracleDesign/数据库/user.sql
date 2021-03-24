create tablespace zjf
  datafile 'D:\zjf.dbf' size 20m
    autoextend on next 5m
    maxsize 100m;

create user zjf
identified by zjf
 default tablespace zjf;

grant dba to zjf;

set pagesize 50
set linesize 150

create table emp as select * from scott.emp;
create table salgrade as select * from scott.salgrade;
create table dept as select * from scott.dept;