create table Account 
( 
AccountNumber  char(18) primary key not null, 
CurrentBalance number not null, 
AsofDate date not null, 
CurrentRate NUMBER (5,2) not null, 
ProductTypeID varchar(40) not null, 
CurrentStatus varchar(40) not null 
);

insert into Account values(1000,5000,sysdate,3.22,12,'active');
insert into Account values(1001,2000,sysdate,2.12,12,'active');
insert into Account values(1002,5500,sysdate,4.25,17,'active');
insert into Account values(1003,5020,sysdate,1.56,17,'active');
insert into Account values(1004,5100,sysdate,2.32,10,'active');
insert into Account values(1005,3000,sysdate,1.62,10,'active');
insert into Account values(1006,3200,sysdate,5.12,12,'active');
insert into Account values(1007,1200,sysdate,1.72,12,'active');
insert into Account values(1008,6200,sysdate,2.91,17,'active');
insert into Account values(1009,7000,sysdate,1.20,10,'active');
insert into Account values(1010,2500,sysdate,3.62,12,'active');
insert into Account values(1011,1050,sysdate,3.78,12,'active');

insert into Account values(Account_seq.currval,2550,sysdate,2.36,12,'active');
