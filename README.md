During my math class, I had the opportunity to develop an algorithm that generates prime numbers using prime numbers.
While my algorithm for generating prime numbers may not be considered revolutionary, it is still a unique solution that showcases my ability to think creatively and analytically.

1. The set $p_k$  contains k prime numbers. 

```math
p_k = \{ p_0, p_1, p_2...p_k \}
```


2. Assume that $\phi$ is an integer bigger than $p_k$ and less than $p_{k+2}$. If $\phi$ is a prime, then $\phi = p_{k + 1}$

3. Let $q = \phi$, Then:

```math
q\cdot P:= \left\{ (p_{0}\phi), (p_{1}\phi), (p_{2}\phi)...(p_{k}\phi) \right\}
```
4. Use the elements in $q\cdot P$ to create a $\left| P_{k}  \right|\times \left| P_{k}  \right|$ matrix according to:


