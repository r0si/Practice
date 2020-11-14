create or replace procedure update_account
(acc_num account.AccountNumber%TYPE,
acc_bal account.CurrentBalance%TYPE,
acc_rate account.CurrentRate%TYPE)
as
begin
update Account set CurrentBalance=acc_bal,CurrentRate=acc_rate where AccountNumber=acc_num;
end update_account;
/

create or replace procedure avg_bal(
acc_pro in number,acc_bal out number)
as
begin
select avg(currentbalance) into acc_bal from account where producttypeid=acc_pro;
exception 
when no_data_found then 
dbms_output.put_line('the product id not exists!');
end avg_bal;
/

set serverout on;
DECLARE
  v_sal account.currentbalance%TYPE;

 BEGIN
   avg_bal(12,v_sal);
   DBMS_OUTPUT.PUT_LINE(v_sal);
END; 
/









