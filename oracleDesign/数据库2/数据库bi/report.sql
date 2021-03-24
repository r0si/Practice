ttitle left '日期：' _date  center  '计算机1181 17 毕宗旺执行Scott.emp报表'  right '页：' format 999 skip 2 sql.pno

btitle center '计算机1181 17 毕宗旺！'

set echo off
set verify off
set pagesize 40
set linesize 200
clear columns

column empno heading '员工编号' format 9999
column ename heading '员工姓名' format A10
column job heading '工作名' format A10
column mgr heading '上级编号' format 9999
column hiredate heading '雇用日期' justify center
column sal heading '员工工资' format l999,999.00
column comm heading '员工奖金' format $999,999.00
column deptno heading '部门号' format 9999999999999

break on deptno
compute count label '部门人数' of empno on deptno
compute sum label '部门工资总和' of sal on deptno
select * from emp order by deptno;

clear columns
ttitle off
btitle off