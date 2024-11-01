Dataset: **Unsupervised**
$$
\mathcal{X} = \set{x_i}_{i=1}^{N} 
$$
Likelihood:
$$
\mathcal{L}(\Phi|\mathcal{X}) = \prod_{i=1}^N p(\mathbf{x}_i | \Phi)
$$
$$
log(\mathcal{L}(\Phi|\mathcal{X})) = \sum_{i=1}^N \log \left( \sum_{k=1}^K p(\mathbf{x}_i | C_k) \, Pr(C_k) \right)
$$
**We have two sets of random variables:**
1. $z=$ cluster memberships (hidden variables)
2. $\Phi=$ parameters: $(\boldsymbol{\mu}_1, \boldsymbol{\mu}_2, \ldots, \boldsymbol{\mu}_K, \Sigma_1, \Sigma_2, \ldots, \Sigma_K)$

## **E-step:**
**Calculate Responsibilities**
Responsibilities can be thought as a matrix of $K*N$. 
Using our previously calculated means and covariances we can get a pdf of the gaussian of each cluster. Then, we can apply these gaussians to the points we have to obtain a score function $g_c$. Afterwards, we calculate the score of each point for all clusters and add it to our **probability matrix**. We can then multiply each datapoints $g_c$ value with the prior $P(c)$. Finally, to normalize the values, we get the row sum and divise each element in the row by the row sum. This results in the matrix such as the following:

|  | $g_1( \ . \ )$ | $g_2( \ . \ )$ | $g_3( \ . \ )$ |
| ---- | ---- | ---- | ---- |
| $P_1$ | 0.2 | 0.6 | 0.2 |
| $P_2$ | 0.2 | 0.5 | 0.3 |
| $P_3$ | 0.1 | 0.7 | 0.2 |
Note: $g_c$ refers to the pdf of the gaussian of cluster $c$.
## **M-Step:** 
**Update Means:**
Lets assume $X = [1, 4, 5]$ 
Using the responsibilities matrix, we calculate row $g_1.x[0], \ g_2.x[1] ...$ and so on.

|  | $g_1( \ . \ )$ | $g_2( \ . \ )$ | $g_3( \ . \ )$ |
| ---- | ---- | ---- | ---- |
| $P_1$ | 0.2*1 | 0.6*1 | 0.2*1 |
| $P_2$ | 0.2*4 | 0.5*4 | 0.3*4 |
| $P_3$ | 0.1*5 | 0.7*4 | 0.2*5 |
Result:

|  | $g_1( \ . \ )$ | $g_2( \ . \ )$ | $g_3( \ . \ )$ |
| ---- | ---- | ---- | ---- |
| sum | 0.2+0.8+0.5 | 0.6+2.0+3.5 | 0.2+1.2+1 |
|  | 1.5 | 6.1 | 2.4 |
Afterwards, we divide these values by the sum of responsibilities for clusters (we sum the column for each cluster)

Result:

|  | $g_1( \ . \ )$ | $g_2( \ . \ )$ | $g_3( \ . \ )$ |
| ---- | ---- | ---- | ---- |
| sum | 1.5 | 6.1 | 2.4 |
| divisor | 0.5 | 1.8 | 0.7 |
| result | 3.0 | 3.388 | 3.428 |

These are our new means.

**Update Covariances:**

update priors
$$
\Phi^{(t+1)} = \underset{\Phi}{\text{arg max }} E\left[\mathcal{L}(\Phi | \mathcal{X}, \mathcal{Z}) | \mathcal{X}, \Phi^{(t)}\right]
$$


