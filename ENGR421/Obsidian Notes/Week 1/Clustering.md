
# Introduction
A clustering problem is where you want to discover the inherent groupings in the data, such as grouping customers by purchasing behavior. Unsupervised.

* A technique used to group similar data points together.
* Definition $x = {x_i}^{N}_{i=1}$
* Fitting best rectangle
* Risk asymmetry
* Model selection
-----
$$
\begin{align}
& p(x) = \sum_{k=1}^{K}{p(x|C_k)Pr(C_k)} \\
& p(x|C_k): \text{Component densities} \\
& Pr(C_k): \text{mixture proportions}
\end{align}
$$
-------
Cluster Membership: *We do not know $y_{ik}$ values!*
$$
y_{ik} = \begin{cases}
1, \text{ if } x_i \text{ belongs to k} \\
0, \text{ otherwise}
\end{cases}
$$
-----
$$
\begin{align}
& \text{Error}=\sum_{i=1}^{N}\sum_{k=1}^{K} b_{ik} ||x_i-\hat{\mu}_k||_2^2 \\


& b_{ik} = 
	\begin{cases} 
		1, & \text{if } \|\mathbf{x}_i - \boldsymbol{\mu}_k\| = \min\limits_{c=1}^K || \mathbf{x}_i - \boldsymbol{\hat{\mu}}_k || \\
		0, & \text{otherwise}
	\end{cases}
\end{align}
$$
-------
# Iterative Algorithm
### **STEP 1:** Estimate the cluster memberships ($\hat{y}_{ik}$)
### **STEP 2:** Estimate the parameters.
------
$$
\begin{align*}
& -\text{Initialize } \boldsymbol{\mu}_1, \boldsymbol{\mu}_2, \ldots, \boldsymbol{\mu}_K \text{ randomly} \\
& -\text{Repeat} \\
& \quad \quad \text{for all } \mathbf{x}_i: \\
& \quad\quad \quad b_{ik} = \begin{cases}
1 & \text{if } \|\mathbf{x}_i - \boldsymbol{\mu}_k\| = \min\limits_{c=1}^K \|\mathbf{x}_i - \boldsymbol{\mu}_c\| \\
0 & \text{otherwise}
\end{cases} \\
& \quad \quad \text{for all } \boldsymbol{\mu}_k: \\
& \quad \quad \quad \boldsymbol{\mu}_k = \frac{\sum_{i=1}^N b_{ik} \mathbf{x}_i}{\sum_{i=1}^N b_{ik}} \\
& - \text{Until Convergence} \\
& \quad \text{if [all } b_{ik} \text{'s stay the same] or [all } \boldsymbol{\mu}_k \text{'s stay the same]}

\end{align*}
$$
-------------
**E**xpectation **M**aximization Algorithm ([[EM Algorithm]])
