create table Confirm_deposit ( 
AccontNumber char(18) primary key, 
OpenName char(20) not null, 
Deposit_date date not null, 
Amount Number not null, 
CurrentBalance number not null, 
CurrentRate NUMBER(5,2) not null, 
CustomerNumber number(10,0) references Customer(CustomerNumber) 
);

insert into Confirm_deposit values(1000,'zjf',sysdate,5000,5000,3.22,10);
insert into Confirm_deposit values(1001,'bzw',sysdate,2000,2000,2.12,11);
insert into Confirm_deposit values(1002,'fwc',sysdate,5500,5700,4.25,12);
insert into Confirm_deposit values(1003,'oen',sysdate,5020,5300,1.56,13);
insert into Confirm_deposit values(1004,'gek',sysdate,5100,5200,2.32,14);
insert into Confirm_deposit values(1005,'cyy',sysdate,3000,3200,1.62,15);
insert into Confirm_deposit values(1006,'srr',sysdate,3200,3700,5.12,16);
insert into Confirm_deposit values(1007,'wkg',sysdate,1200,2000,1.72,17);
insert into Confirm_deposit values(1008,'gnt',sysdate,6200,7000,2.91,18);
insert into Confirm_deposit values(1009,'elc',sysdate,7000,8400,1.20,19);

