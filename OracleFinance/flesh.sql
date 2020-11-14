create table Flesh_deposit ( 
AccountNumber char(18) primary key, 
OpenName char(20) not null,  
Deposit_date date not null, 
Amount Number not null, 
CurrentBalance number not null, 
CurrentRate NUMBER (5,2) not null, 
CustomerNumber number(10,0)  references Customer(CustomerNumber) 
);

insert into flesh_deposit values(1000,'zjf',sysdate,6000,6500,3.22,10);
insert into flesh_deposit values(1001,'bzw',sysdate,8000,8400,3.12,11);
insert into flesh_deposit values(1002,'fwc',sysdate,5100,5700,4.25,12);
insert into flesh_deposit values(1003,'oen',sysdate,5000,5300,2.56,13);
insert into flesh_deposit values(1004,'gek',sysdate,5100,5400,2.32,14);
insert into flesh_deposit values(1005,'cyy',sysdate,3000,3800,3.62,15);
insert into flesh_deposit values(1006,'srr',sysdate,3200,3700,5.12,16);
insert into flesh_deposit values(1007,'wkg',sysdate,1200,2000,4.72,17);
insert into flesh_deposit values(1008,'gnt',sysdate,6200,7000,2.91,18);
insert into flesh_deposit values(1009,'elc',sysdate,7000,8400,3.20,19);
