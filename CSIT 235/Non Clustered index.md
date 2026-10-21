---
index: true
course: "CSIT 235"
chapter: "Database indexing"
concept: "Non Clustered index"
---

# Non Clustered index

- index are ordered indirectly in a [[BStar Tree]]
- keys are referenced by RIDS (row identifiers) stored separately 
- RIDS are used as they are unique (Non unique values allowed )

##### Key benefit
- Non clustered index can be specified to certain ranges via using WHERE clauses (stating conditions)
- More than one non clustered index can exist

| pros                      | cons                                                  |
| ------------------------- | ----------------------------------------------------- |
| fast insert speed         | Slow reading speeds on ranges, slow sorting operation |
| fast update speed         |                                                       |
| fast read(matching) speed |                                                       |
>[!explanation]-
>- The order at which the [[Secondary index]] is arranged is separate from the table. Searching can be easier if values is numerical
>- operations are faster as only the RID has to be updated rather than the entire row
>- Slow for ranges and sorting, RID has to refer back to table for each comparison

### Structure
- Rows of the mapped columns are referenced by RID
- RID is arranged separate from the table
![[Pasted image 20250531232929.png|500]]
### Use case
- For small, frequently queries values 
- Non primary key columns
