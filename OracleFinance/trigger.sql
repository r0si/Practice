CREATE OR REPLACE TRIGGER tri_time
BEFORE INSERT OR DELETE OR UPDATE ON customer
disable
BEGIN
 IF (TO_CHAR(sysdate,'DAY') IN ('Saturday', 'Sunday')) OR (TO_CHAR(sysdate, 'HH24:MI') NOT BETWEEN '8:30' AND '18:00') THEN
     RAISE_APPLICATION_ERROR(-20001, 'do not during change customer');
 END IF;
END;
/









CREATE OR REPLACE TRIGGER tri_update
    AFTER UPDATE OF PRODUCTTYPEID,CURRENTBALANCE OR INSERT OR DELETE
    ON account
BEGIN
    IF INSERTING OR DELETING THEN
        DBMS_OUTPUT.PUT_LINE('the delete or insert is !');
        FOR v_proid IN (SELECT PRODUCTTYPEID, count(*) v_count FROM account GROUP BY PRODUCTTYPEID )
            LOOP
                DBMS_OUTPUT.PUT_LINE(v_proid.PRODUCTTYPEID || '  ' || v_proid.v_count);
            END LOOP;
    ELSIF UPDATING ('CURRENTBALANCE') THEN
        DBMS_OUTPUT.PUT_LINE('the trigger is updating CURRENTBALANCE！');

        FOR v_probal IN (SELECT PRODUCTTYPEID, avg(CURRENTBALANCE) v_bal
                         FROM account
                         GROUP BY PRODUCTTYPEID
                         order BY PRODUCTTYPEID)
            LOOP
                DBMS_OUTPUT.PUT_LINE(v_probal.PRODUCTTYPEID || '  ' || v_probal.v_bal);
            END LOOP;
    ELSE
        DBMS_OUTPUT.PUT_LINE('the product id is changing!');
        FOR v_proid IN (SELECT PRODUCTTYPEID, count(*) v_count FROM account GROUP BY PRODUCTTYPEID)
            LOOP
                DBMS_OUTPUT.PUT_LINE(v_proid.PRODUCTTYPEID || '  ' || v_proid.v_count);
            END LOOP;
    END IF;
END tri_update;
/

CREATE OR REPLACE TRIGGER tri_take
 AFTER DELETE OR INSERT OR UPDATE ON take
DECLARE
 V_TYPE takelog.L_TYPE%TYPE;
BEGIN
 IF INSERTING THEN
  V_TYPE := 'INSERT';
  DBMS_OUTPUT.PUT_LINE('The record was inserted successfully and logged');
 ELSIF UPDATING THEN
  V_TYPE := 'UPDATE';
  DBMS_OUTPUT.PUT_LINE('The record has been successfully updated and logged');
 ELSIF DELETING THEN
  V_TYPE := 'DELETE';
  DBMS_OUTPUT.PUT_LINE('The record has been successfully deleted and logged');
 END IF;
 INSERT INTO takelog
 VALUES
  (USER, V_TYPE, TO_CHAR(SYSDATE, 'yyyy-mm-dd hh24:mi:ss'));
END;
/