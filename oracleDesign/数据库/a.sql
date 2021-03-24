create tablespace zyr
 datafile 'd:\zyr.dbf' size 10m
  autoextend on next 10m 
  maxsize 40m;


--alter tablespace zyr 
--add datafile 'd:\zyr1.dbf'  size 20m
--autoextend on next 5m maxsize 50m;


create  user zyr
identified by zyr
default tablespace zyr;



grant dba to zyr;



/