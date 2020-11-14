SET SERVEROUTPUT ON 
DECLARE 
v_account ACCOUNT.accountnumber %TYPE; 
v_balance ACCOUNT.currentbalance %TYPE; 
v_proid ACCOUNT.PRODUCTTYPEID %TYPE;
CURSOR cur_acc IS SELECT accountnumber,currentbalance FROM account where PRODUCTTYPEID= v_proid; 

BEGIN 
v_proid:=&x;
OPEN cur_acc;
LOOP
FETCH cur_acc INTO v_account,v_balance; 
EXIT WHEN cur_acc%NOTFOUND;
DBMS_OUTPUT.PUT_LINE('the '||cur_acc%rowcount||' Account of Customer '||v_account||' is '||v_balance); 
END loop;
CLOSE cur_acc; 
END; 
/ 


DECLARE
    CURSOR c_cursor
        IS SELECT accountnumber, currentbalance
           FROM account
           WHERE rownum < 11;
    v_ename account.accountnumber%TYPE;
    v_sal   account.currentbalance%TYPE;
BEGIN
    OPEN c_cursor;
    FETCH c_cursor INTO v_ename, v_sal;
    WHILE c_cursor%FOUND
        LOOP
            DBMS_OUTPUT.PUT_LINE(v_ename || '---' || v_sal);
            FETCH c_cursor INTO v_ename, v_sal;
        END LOOP;
    CLOSE c_cursor;
END;
/