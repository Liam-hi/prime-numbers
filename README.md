## Introduction:

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

```math
\begin{pmatrix}
 22 mod 2&22mod3  &22mod5  &22mod7  \\
33mod2 & 33mod3 & 33mod5 & 33mod7 \\
 55mod2&  55mod3&  55mod5&  55mod7\\
 77mod2& 77mod3 & 77mod5 & 77mod7
\end{pmatrix}=\begin{pmatrix}
 0&1 &2 &1 \\
1& 0 & 3& 5 \\
 1&  1&  0&  6\\
 1& 2& 2 & 0
\end{pmatrix}
```

## Example: 

1. $p_14$ generates the matrix

```math
\begin{pmatrix}
 0&  1&  4&  3&  6& 3 & 9 & 18 & 2 & 7 & 1 &20  &  12 &  8 \\
 1& 0 & 1 & 1 & 9 & 11 & 5 & 8 & 3 & 25 & 17 & 30 & 18 & 12 \\
 1 &1 & 0 & 4 & 4 & 1 &14 & 7 & 5&  3& 18& 13& 30 &20  \\
  1 & 2 & 4 & 0& 10 & 4&  6 & 6 & 7& 10& 19& 33 & 1 &28  \\
 1 & 1 & 2  &6 & 0 &10 & 7 & 4 &11 &24& 21 &36 &25  &1  \\
 1  &2  &1 & 2 & 6 & 0& 16 & 3 &13 & 2& 22 &19& 37  &9  \\
 1 & 1 & 4 & 1&  7 & 6 & 0 & 1 &17 &16 &24 &22 &20 &25 \\
  1 & 2 & 3 & 4 & 2 & 9 & 9 & 0 &19& 23 &25 & 5 &32& 33 \\
 1  &1 & 1 & 3 & 3 & 2 &10 &17 & 0 & 8& 27 & 8 &15  &6 \\
  1 & 1 & 3 & 5 &10& 11 & 3& 14 & 6 & 0 &30& 31 &10 &30 \\
 1 & 2 & 2 & 1 & 5 & 1 &12& 13 & 8 & 7 & 0 &14 &22 &38 \\
 1  & 2 &  4 & 3  &1& 10 & 5 &10 &14 &28 & 3 & 0 &17 &19 \\
 1 & 1 & 2 & 2 & 2 & 3 & 6 & 8 &18& 13&  5 & 3 & 0 &35 \\
 1 & 2 & 1 & 5 & 8 & 6 & 15 & 7& 20& 20 & 6 &23 &12  &0
\end{pmatrix}
```

## Thoughts 

Let us look at the first prime numbers, 2 and 3. If $P = \left\{ 2, 3 \right\}$ and $q = 4$ generates a singular matrix, change  to 5. If   and  generates a matrix whose diagonal element are all equal to zero (only zeros on diagonal) and nonsingular, change  to . Now let us look at  and  (we can skip  because  is an even number ).  and  generates a valid matrix so we can change  to .  and  generates a singular matrix so we can move to 



