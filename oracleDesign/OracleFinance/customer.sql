create table Customer(
  CustomerNumber number(10,0) primary key not null,
  CustomerName varchar(20) not null,
  CustomerSex nchar(1) not null,
  CustomerDate char(10) not null,
  CustomerAge char(10),
  CustomerNative char(18) not null,
  CustomerIDCard char(18) not null,
  LinkTelephone char(18) not null
);

insert into Customer values(10,'zjf','M',sysdate,20,'hubei',429001200005280013,17720275137);
insert into Customer values(11,'bzw','F',sysdate,21,'hubei',350201198701146613,15219466201);
insert into Customer values(12,'fwc','M',sysdate,20,'sichuan',350212197604048290,17008803333);
insert into Customer values(13,'oen','M',sysdate,20,'henan',350211198903056176,15036222256);
insert into Customer values(14,'gek','F',sysdate,20,'beijing',350205199112281411,18438888133);
insert into Customer values(15,'cyy','M',sysdate,20,'guangdong',350203198904175513,18876941131);
insert into Customer values(16,'srr','F',sysdate,20,'hongkong',350201198109028634,18876622089);
insert into Customer values(17,'wkg','F',sysdate,20,'taiwan',350205198804137117,13715150077);
insert into Customer values(18,'gnt','M',sysdate,20,'shenzhen',350213199201221912,17703771999);
insert into Customer values(19,'elc','M',sysdate,20,'shanghai',350201199112208796,18351078990);
