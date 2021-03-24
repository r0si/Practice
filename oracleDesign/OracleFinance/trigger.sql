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
