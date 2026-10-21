---
index: true
course: "CSCI203"
chapter: "Algorithm analysis"
concept: "runtime complexity"
---

# runtime complexity

Runtime complexity is the processing time needed relative to the size of the data *n*.

![[Pasted image 20250109161446.png]]
[[masternote 123|Refer to vonn nuemans model]]

## calculation of runtime complexity

| processes              | Average runtime (according to *n*)                  | Best runtime | Worst runtime |
| ---------------------- | --------------------------------------------------- | ------------ | ------------- |
| For loop/While loop    | n                                                   | ==           | ==            |
| Conditionals           | 0 or 1                                              | ==           | ==            |
| [[Recursion]]          | a^(n)     *where a is the number of recursive call* | n            | 2^n           |
| [[Divide and conquer]] | nlogn                                               | n            | 2^n           |
> [!example]- Example
> ![[Pasted image 20250109165601.png]]
> a, b and c are all variables assigned to conditionals in the program
> a --> if string1 length != string2 length
> b --> if j is not marked and i = j
> c --> if matched = False
>
> d is erroneous as it will always execute so it should be denoted as 1.
>
> ##### calculation
> 𝑇 𝑛 = 1 + 𝑎 + 𝑛 + 1 + 𝑛 + (𝑛 2+𝑛) + (𝑛 2 ) + 𝑏 + 𝑏 + 𝑏 + 𝑛 + 𝑐 + 1
> assuming *worst case scenario*,
> a = 0
> b = n
> c = 0
> d = 1
>
> ***results:***
> 𝑻 𝒏 = 𝟐𝒏 𝟐 + 𝟕𝒏 + 𝟑
>
### Growth rates
![[asymptotic growth rate]] 
