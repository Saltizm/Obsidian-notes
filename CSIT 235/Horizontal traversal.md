- Traversing across the leaf nodes of a [[Index Data structure|index]] like a [[linked list]] 
- reserved for:
	- Full table scans
	- Operations
### Example
#### Full table scan
```sql
SELECT * FROM SampleTable;
```
#### Operations
```sql
SELECT * FROM SampleTable
WHERE col2>100;

SELECT * FROM SampleTable
ORDER BY col2;

SELECT col1, MAX(col2) FROM SampleTable
GROUP BY col1;
```
