set SERVEROUTPUT on;
DECLARE
  v_sal emp.sal%type;
 v_ename emp.ename%type;

BEGIN
v_ename:=&x;

 select sal into v_sal from emp where ename =v_ename;
DBMS_OUTPUT.PUT_LINE(v_ename || '员工工资为: '||v_sal); 

EXCEPTION
  
WHEN NO_DATA_FOUND THEN
     DBMS_OUTPUT.PUT_LINE('There is not such an employee!');
  WHEN TOO_MANY_ROWS THEN 
    FOR v_emp IN (SELECT * FROM emp WHERE  ename=v_ename ) LOOP
       DBMS_OUTPUT.PUT_LINE(v_emp.empno||'ename：'|| v_emp.ename || 'sal：' || v_emp.sal );
    END LOOP;
END;
/
