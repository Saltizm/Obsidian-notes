- an attribute set is a collection of attributes that describe all the characteristics of an entity in a domain through [[Functional Dependancy|functional dependancies]] 
- an attribute set is closed if all attribute is *Functionally dependent* on one *primary key*
### Algorithm
$X^+ = X$
While $X^+ \neq \triangle$ :
	For $FD,Y\rightarrow Z$ in $F$:
		if $Y \subseteq X^+$:
			$X^+ =X^+ \cup Z$ 

$X^+$ is the Primary key.
##### In practice 
Consider R(A,B,C,D,E,F,G) with the [[Functional Dependancy]]:
$A \rightarrow BC$
$BC \rightarrow DE$
$D \rightarrow F$
$CF \rightarrow G$

$\{A\}^+$= $\{A, B, C\}$                        ($A \rightarrow BC$)
	= $\{A, B, C, D, E\}$               ($BC \rightarrow DE$)
	=$\{A, B, C, D, E, F\}$            ($D \rightarrow F$)
	=$\{A, B, C, D, E, F, G\}$        ($CF \rightarrow G$)



