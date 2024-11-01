**Definition:**
$$
y=f(x)+\epsilon
$$

**Goal:** Estimate $f(x)$ with $g(x|\theta)$ 
**Assumptions:** 
	1. $p(\epsilon) ~N(\epsilon; 0, \sigma^2)$
	2. $p(y|x) \sim N(y; g(x|\theta), \sigma^2)$
		$y|x \rightarrow f(x) + \epsilon$
		$y|x \rightarrow g(x|\theta) + \epsilon$


**Likelihood:** $l(\theta | X):$ $$\prod_{i=1}^N {p(x_i,y_i)} = \prod_{i=1}^N {p(y_i|x_i)p(x_i)}$$
**Loglikelihood** $L(\theta|X):$ $$\sum_{i=1}^N{log(p(y_i|x_i)) + log(p(x_i))}$$
$log(p(x_i)): \text{  is a constant so we can get rid of it}$

**Goal:** Maximize the likelihood
$$\sum_{i=1}^N{log(p(y_i|x_i))} = \sum_{i=1}^N{log(N(y;\mu,\sigma^2))}$$Applying the normal distribution, and getting rid of constants, we are left with:
$$
-\sum_{i=1}^N{(y_i-g(x_i|\theta))^2} = -\sum_{i=1}^N{(y_i-\hat{y}_i)^2} = -\sum_{i=1}^N{e_i^2}
$$

**Minimize:** $$ \sum_{i=1}^N{e_i^2} $$
After taking the determinants for $w_0$ and $w_1$ the equation becomes: 
**Linear Assumption:**
$$
g(x_i|\theta) = w_o+w_1x_i
$$
Taking the derivatives by  $dw_0, dw_1$
$$
\frac{ d \sum_{i=1}^N{(y_i-\hat{y}_i)^2}}{dw_0} = \frac{ d\sum_{i=1}^N{[y_i-(w_0+w_1.x_i)]}}{dw_o} 
$$
$$
\sum_{i=1}^Ny_i = \sum_{i=1}^Nw_o+\sum_{i=1}^Nw_1x
$$
Similarly for $\frac{d\sum_{i=1}^Ne^2_n}{dw_1}$:
$$
\sum_{i=1}^N(y_ix_i) = \sum_{i=1}^Nw_0x_i+\sum_{i=1}^Nw_1x_i^2
$$

We can write these two equations in the following form:
$$
\begin{bmatrix}
\sum_{i=1}^Ny_i  \\
\sum_{i=1}^Ny_ix_i
\end{bmatrix}
=
\begin{bmatrix}
\sum_{i=1}^N1 \ \sum_{i=1}^Nx_i \\
\sum_{i=1}^Nx_i \ \sum_{i=1}^Nx_i^2
\end{bmatrix}

\begin{bmatrix}
w_0  \\
w_1
\end{bmatrix}
$$
$$
b = A.\theta
$$
If we can find $A^{-1}$, we can write the equation as the following:
$$
\begin{align}
A^{-1}b &= A^{-1}A . \theta \\
A^{-1}.b &=\theta^*
\end{align}
$$

---
## Polynomial Regression

$\text{poly\_regression}(x, y, K=1) = \text{lin\_regression}(x, y)$


$$
g(x|\theta):=w_o+w_1x+w_2x^2...w_nx^n
$$

![[Pasted image 20231124234650.png]]
#Bored : Turn this image to latex.

Taking the derivatives of $g(x|\theta)$ with respect to all $\theta$, we get k+1 equations, which can be written as follows:
$$
\begin{align}
\bf A\theta = b \\
\bf aw = y
\end{align}
$$
![[Pasted image 20231124235114.png]]