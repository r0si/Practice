ttitle left '日期：' _date  center  '张剑飞执行Scott.emp报表'  right '页：' format 999 skip 2 sql.pno

btitle center '计算机1181 04 张剑飞！'

set echo off
set verify off
set pagesize 40
set linesize 130
clear columns

column empno heading '员工编号' format 9999
column ename heading '员工姓名' format A10
column job heading '职位' format a10
column mgr heading '上级编号' format 9999
column hiredate heading '雇佣日期' justify center
column sal heading '员工工资' format L999,999.99
column comm heading '奖金' format $999,999.99
column deptno heading '部门名' format 999999999999


break on deptno
compute sum label '员工工资总合' of sal on deptno
compute count label '部门人数' of empno on deptno
select * from scott.emp order by deptno;

clear columns
ttitle off
btitle off