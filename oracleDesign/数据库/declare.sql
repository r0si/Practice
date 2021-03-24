set SERVEROUTPUT on;

declare
emp_number constant number(4):=8888;
emp_name varchar2(10);
emp_job varchar2(9);
emp_sal number(7,2);
emp_mgr number(4);
emp_hiredate date;
emp_comm number(7,2);
emp_deptno number(2);

begin
select ename ,job ,mgr,hiredate,sal,comm,deptno    --表格数据列
into emp_name,emp_job,emp_mgr,emp_hiredate,emp_sal,emp_comm,emp_deptno               --块中定义的变量
from emp
where empno=emp_number;

DBMS_OUTPUT.PUT_LINE ('查询员工的编号为：'||emp_number);
DBMS_OUTPUT.PUT_LINE ('查询员工的姓名为：'||emp_name);
DBMS_OUTPUT.PUT_LINE ('查询员工的工作岗位为：'||emp_job);
DBMS_OUTPUT.PUT_LINE ('查询员工的上司编号为：'||emp_mgr);
DBMS_OUTPUT.PUT_LINE ('查询员工的雇用时间为：'||emp_hiredate);
DBMS_OUTPUT.PUT_LINE ('查询员工的工资为：'||emp_sal);
DBMS_OUTPUT.PUT_LINE ('查询员工的奖金为：'||emp_comm);
DBMS_OUTPUT.PUT_LINE ('查询员工的部门编号为：'||emp_deptno);
end;
26
/