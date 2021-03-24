

CREATE OR REPLACE FUNCTION func_maxbal(p_proid account.producttypeid%TYPE)
  return account.currentbalance%TYPE
AS
  v_maxbal account.currentbalance%TYPE;
BEGIN
  SELECT max(currentbalance) INTO v_maxbal FROM account
   WHERE producttypeid=p_proid ; 
  RETURN v_maxbal;
EXCEPTION 
  WHEN NO_DATA_FOUND THEN
     DBMS_OUTPUT.PUT_LINE('The product id is invalid! ');
END func_maxbal;
/

