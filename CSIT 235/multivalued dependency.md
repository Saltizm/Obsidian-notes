- Multivalued dependency is when a single value has multiple MCK([[Minimal key|minimal ]][[Candidate key|candidate]] key) that are **independent** from each other.
### Example
- Session(Student, Lesson, Professor)
- There are 2 MCK 
	- Student, Lesson
	- Professor, Lesson
- This can be broken down into
- Lesson is taught to MANY students
- Lesson is taught to MANY Professor
