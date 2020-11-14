create tablespace zjf
  datafile 'zjf.dbf' size 20m
    autoextend on next 5m
    maxsize 100m;
   
create user zjf
identified by zjf
 default tablespace zjf;

grant dba to zjf;


create user sr
identified by sr
 default tablespace zjf;
 
 create user cyy
identified by cyy
 default tablespace zjf;
 
 create user bzw
identified by bzw
 default tablespace zjf;
 
 create role users;
 grant create session to users;
 
 grant users to cyy;
 grant users to sr;
 grant users to bzw;
 
 
 create role manager;
grant alter any table to manager;
grant insert any table to manager;
grant create session to manager;

create user admin
identified by admin
 default tablespace zjf;

grant manager to admin; 
 
 
