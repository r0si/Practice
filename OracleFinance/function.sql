CREATE OR REPLACE FUNCTION func_maxbal(p_proid account.producttypeid%TYPE)
  return account.currentbalance%TYPE
AS
  v_maxbal account.currentbalance%TYPE;
BEGIN
  SELECT max(currentbalance) INTO v_maxbal FROM account
   WHERE producttypeid=p_proid; 
  RETURN v_maxbal;
EXCEPTION
  WHEN NO_DATA_FOUND THEN
     DBMS_OUTPUT.PUT_LINE('The product id is invalid!');
END func_maxbal;
/

CREATE OR REPLACE FUNCTION get_balance(proid account.producttypeid%TYPE)
    RETURN NUMBER
    IS
    V_sum NUMBER;
BEGIN
    SELECT SUM(currentbalance)
    INTO V_sum
    FROM account
    WHERE producttypeid = proid;
    RETURN V_sum;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('The data you need doesnt exist!');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE(SQLCODE || '---' || SQLERRM);
END get_balance;
/

