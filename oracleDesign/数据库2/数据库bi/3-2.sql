alter table dept add constraint sys001  primary key(deptno);--给dept表添加主键
alter table emp add constraint sys002  primary key(empno);--给emp表添加主键
alter table emp add constraint sys003 foreign key(deptno) references dept(deptno);--给emp表添加外键
--查询emp表的约束
select a.table_name, a.column_name, a.constraint_name ,b.constraint_type
from  user_cons_columns a, user_constraints b
where a.table_name='EMP'  and  a.constraint_name=b.constraint_name;
