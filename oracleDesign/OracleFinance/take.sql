create table Take ( 
AccountNumber  char(18) primary key not null, 
CurrentBalance char(20) not null, 
OutDate date not null, 
OutAmount number not null, 
LessAmount number not null 
);

insert into Take values(1000,5000,sysdate,0,5000);
insert into Take values(1001,2000,sysdate,0,2000);
insert into Take values(1002,5500,sysdate,0,5500);
insert into Take values(1003,5020,sysdate,0,5020);
insert into Take values(1004,5100,sysdate,0,5100);
insert into Take values(1005,3000,sysdate,0,3000);
insert into Take values(1006,1200,sysdate,0,1200);
insert into Take values(1007,6200,sysdate,0,6200);
insert into Take values(1008,7000,sysdate,0,7000);
insert into Take values(1009,2500,sysdate,0,2500);
