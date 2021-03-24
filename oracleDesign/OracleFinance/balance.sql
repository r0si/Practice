create table Balance
(
  AccountNumber char(18) primary key not null,
  Password char(50) not null,
  CurrentBalance char(20) not null,
  SelectDate date not null
);


insert into balance values(1000,md5(1),5000,sysdate);
insert into balance values(1001,md5(2),2000,sysdate);
insert into balance values(1002,md5(3),5500,sysdate);
insert into balance values(1003,md5(4),5020,sysdate);
insert into balance values(1004,md5(5),5100,sysdate);
insert into balance values(1005,md5(6),3000,sysdate);
insert into balance values(1006,md5(7),3200,sysdate);
insert into balance values(1007,md5(8),1200,sysdate);
insert into balance values(1008,md5(9),6200,sysdate);
insert into balance values(1009,md5(10),7000,sysdate);
insert into balance values(1010,md5(11),2500,sysdate);


CREATE OR REPLACE FUNCTION MD5(pass IN VARCHAR2)
RETURN VARCHAR2 IS v VARCHAR2(32);
BEGIN
  v:=utl_raw.cast_to_raw(DBMS_OBFUSCATION_TOOLKIT.MD5(INPUT_STRING => pass));
RETURN v;
END;  
/


