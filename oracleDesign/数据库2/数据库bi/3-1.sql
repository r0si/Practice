--查询约束
select a.table_name, a.column_name, a.constraint_name ,b.constraint_type
from  user_cons_columns a, user_constraints b
where a.table_name='DEPARTMENTS'  and  a.constraint_name=b.constraint_name;
--删除外键约束
alter table departments drop constraint SYS_C0011395;
--给departments添加外键alter table departments add constraint SYS003 foreign key(location_id) references locations(location_id);
--如果报ORA-02298: 无法验证 (BZW.SYS003) - 未找到父项关键字，可能是那个location的主键删除了，给locations重新设置主键
--创建序列
create sequence se1 start with 10000 increment by 1 maxvalue 99999 minvalue 10000 order;
create sequence se2 start with 10 increment by 10 maxvalue 990 minvalue 10 order;	
--插入数据
insert into departments values(se2.nextval,'cs',2,4);
insert into departments values(se2.nextval,'cs',3,5);
--如果报错ora-02291：违反完整的约束的条件，（bzw_sys_c0011405）未找父项关键字，就把sys_c0011405删掉
insert into employees values(se1.nextval,'b','zw','BZWS','123', to_date ( '2007-11-15' , 'YYYY-MM-DD' ),1,800,0.12,1,10);
insert into employees values(se1.nextval,'b1','zw1','FAHFAFS','124', to_date ( '2007-11-15' , 'YYYY-MM-DD' ),2,801,0.13,2,10);
insert into employees values(se1.nextval,'b2','zw2','FASFA','125', to_date ( '2007-11-15' , 'YYYY-MM-DD' ),3,802,0.11,3,10);
--查询数据
select * from departments;
select * from employees;