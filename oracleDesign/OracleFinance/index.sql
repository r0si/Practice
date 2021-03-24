create index index_num
on account (account_number asc);

create index namelower_index on customer (lower(customername));
