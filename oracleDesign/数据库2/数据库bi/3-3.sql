--插入数据
insert into emp values(8888,'毕宗旺','student',8888,to_date('03-03-2020','DD-MM-YY'),8888,8888,10);
--创建匿名块
set SERVEROUTPUT on;

declare 
emp_number constant number(4):=8888;
emp_name varchar2(10);
emp_job varchar2(9);
emp_mgr number(4);
emp_hiredate date;
emp_sal number(7,2);
emp_comm number(7,2);
emp_deptno number(2);

begin
select ename,job,mgr,hiredate,sal,comm,deptno 
into emp_name,emp_job,emp_mgr,emp_hiredate,emp_sal,emp_comm,emp_deptno 
from emp 
where empno=emp_number;
DBMS_OUTPUT.PUT_LINE ('我的编号-->'||emp_number);
DBMS_OUTPUT.PUT_LINE ('我的姓名-->'||emp_name);
DBMS_OUTPUT.PUT_LINE ('我的职业-->'||emp_job);
DBMS_OUTPUT.PUT_LINE ('我的上级编号-->'||emp_mgr);
DBMS_OUTPUT.PUT_LINE ('我的雇佣日期-->'||emp_hiredate);
DBMS_OUTPUT.PUT_LINE ('我的工资-->'||emp_sal);
DBMS_OUTPUT.PUT_LINE ('我的奖金-->'||emp_comm);
DBMS_OUTPUT.PUT_LINE ('我的系号-->'||emp_deptno);
END;
/


--使用%type的方法
set SERVEROUTPUT on;
declare 
emp_number constant emp.empno%type:=8888;
emp_name emp.ename%type;
emp_job emp.job%type;
emp_sal emp.sal%type;
emp_mgr emp.mgr%type;
emp_hiredate emp.hiredate%type;
emp_comm emp.comm%type;
emp_deptno emp.deptno%type;
begin
select ename,job,mgr,hiredate,sal,comm,deptno
into emp_name,emp_job,emp_mgr,emp_hiredate,emp_sal,emp_comm,emp_deptno from emp
where empno=emp_number;
DBMS_OUTPUT.PUT_LINE ('我的编号-->'||emp_number);
DBMS_OUTPUT.PUT_LINE ('我的姓名-->'||emp_name);
DBMS_OUTPUT.PUT_LINE ('我的职业-->'||emp_job);
DBMS_OUTPUT.PUT_LINE ('我的上级编号-->'||emp_mgr);
DBMS_OUTPUT.PUT_LINE ('我的雇佣日期-->'||emp_hiredate);
DBMS_OUTPUT.PUT_LINE ('我的工资-->'||emp_sal);
DBMS_OUTPUT.PUT_LINE ('我的奖金-->'||emp_comm);
DBMS_OUTPUT.PUT_LINE ('我的系号-->'||emp_deptno);
end;
/


--使用%rowtype的方法
set SERVEROUTPUT on;
declare 
emp_number constant emp.empno%type:=8888;
oneemp emp%rowtype;
begin
select *
into oneemp
from emp
where empno=emp_number;
DBMS_OUTPUT.PUT_LINE ('查询员工的编号为：'||emp_number);
DBMS_OUTPUT.PUT_LINE ('查询员工的为：'||oneemp.ename);
DBMS_OUTPUT.PUT_LINE ('查询员工的工作为：'||oneemp.job);
DBMS_OUTPUT.PUT_LINE ('查询员工的薪水为：'||oneemp.sal);
DBMS_OUTPUT.PUT_LINE ('查询员工的部门号为：'||oneemp.mgr);
DBMS_OUTPUT.PUT_LINE ('查询员工的雇佣日期为：'||oneemp.hiredate);
DBMS_OUTPUT.PUT_LINE ('查询员工的奖金为：'||oneemp.comm);
DBMS_OUTPUT.PUT_LINE ('查询员工的系为：'||oneemp.deptno);
end;
/




