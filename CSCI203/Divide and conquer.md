Divide and conquer algorithms is a method used in computer science to solve big problems by breaking them down (*divide*) into smaller parts, and solving and combining (*conquer*) them into the final output.

<h2>Similarity to Recursion algorithms</h2>
although structurally similar to [[Recursion|recursive algorithms]], DnC algorithms have a better average [[runtime complexity]]. 
![[Pasted image 20250109164200.png]]
<h3>log n</h3>
on average all partitions are split 1/3 or 2/3 ways due to the randomly chosen pivot.
this follows the logarithmic progression.

<h3>n</h3>
during the *conquer* part, the algorithm has to run through the entire array *n* once to combine all of the partitions.