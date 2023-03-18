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


```math
\begin{pmatrix}
 \phi p_{0}modp_{0} &  \phi p_{0}modp_{1}  &\phi p_{0}modp_{2} & ... & ... &  \phi p_{0}modp_{k}  \\
 \phi p_{1}modp_{0} &  \phi p_{1}modp_{1}  &\phi p_{1}modp_{2} & ... & ... &  \phi p_{1}modp_{k}  \\
 \phi p_{2}modp_{0} &  \phi p_{2}modp_{1}  &\phi p_{2}modp_{2} & ... & ... &  \phi p_{2}modp_{k}  \\
 . &. & . & . & . & .  \\
 . &. & . & . & . & .  \\
 . &. & . & . & . & .  \\
 \phi p_{k}modp_{0} &  \phi p_{k}modp_{1} & . & . & . & \phi p_{k}modp_{k}  & 
\end{pmatrix}
```

## Example:

1. The set $p_4$ contains the first 4 prime numbers. 

```math
P_{4} = \left\{ 2, 3, 5, 7 \right\}
```

2. Let $q = 11$ . 11 is bigger than 7 and less than 13. Then:

```math
q\cdot P:= \left\{(2\cdot 11), (3\cdot 11), (5\cdot 11),  (7\cdot 11) \right\} =  \left\{(22), (33), (55),  (77) \right\}
```
3. Create a $\left| P_{4}  \right|\times \left| P_{4}  \right| = 4 \times 4$ matrix. 
