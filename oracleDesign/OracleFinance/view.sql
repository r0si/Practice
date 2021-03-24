create or replace view acc_view
as
select * from account where currentbalance>=6000;

create or replace view flesh_view
as
select count(producttypeid) product_12_count from account where producttypeid=12;


