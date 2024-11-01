![[Pasted image 20231218171540.png|500]]

# Defining Margin Constraints
$$
\frac{r^t (\textbf{w}^T x^i + w_0)}{\|\textbf{w}\|_2} \geq \rho, \forall i
$$
Where ${\|\textbf{w}\|_2}=\text{magnitude of vector}$ 
# Objective Function Formulation
We want the hyperplane to be $\rho$ away from all of the points.

## Standardizing the SVM Problem
We want to maximize $\rho$, but there are infinite solutions through scaling $\textbf{w}$. To obtain a **unique solution**, we set $|\mathbf{w}|_2 .\rho = 1$.

## Unique Solution through Norm Minimization
$$
\min \frac{1}{2} \|\mathbf{w}\|_2^2 \text{ subject to } r^t (\mathbf{w}^T x^t + w_0) \geq +1, \forall t
$$

# Lagrangian Method in SVM

The Lagrangian $\mathcal{L}(x, \lambda)$ is formulated by combining the objective function and the constraint with a Lagrange multiplier $\lambda$. The constraint is rewritten as $g(x)$, and the Lagrangian is: $\mathcal{L}(x, \lambda) = f(x) - \lambda \cdot g(x)$

# Primal Problem Derivation
## Formulation:
$$
\begin{aligned}
& \text{minimize}
& & \frac{1}{2}\|\mathbf{w}\|^2_2 \\
& \text{subject to:}
& & y_i (\mathbf{w}^T x_i + w_0) \geq 1 \quad \forall i \\
& \text{Decision variables:} 
& & \set{\textbf{w}, w_o}
\end{aligned}
$$

# Lagrangian Primal (LP) Expression
$$
\mathcal{L}_P = \frac{1}{2} \mathbf{w}^T\mathbf{w} - \sum_{i=1}^{N} \alpha_i \left[ y_i \left( \mathbf{w}^T x_i + w_0 \right) - 1 \right]
$$
**Role of Lagrange Multipliers:**
In the context of SVM, it allows us to solve for the weight vector ww and bias w0w0​ more efficiently by considering only the support vectors, which are the data points that lie on the margins.
# Derivatives and Critical Points
$$
\mathbf{w}: \ \frac{\partial \mathcal{L}_P}{\partial \mathbf{w}} = \frac{1}{2} \cdot 2 \mathbf{w} - \sum_{i=1}^{N} \alpha_i y_i x_i = 0 \Rightarrow \mathbf{w} = \sum_{i=1}^{N} \alpha_i y_i x_i
$$
$$
w_0: \ \frac{\partial \mathcal{L}_P}{\partial w_0} = - \sum_{i=1}^{N} \alpha_i y_i = 0 \Rightarrow \sum_{i=1}^{N} \alpha_i y_i = 0
$$
# Extended Lagrangian Formulation
$$
\begin{aligned}
\mathbf{w}^T\mathbf{w} &= \left( \sum_{i=1}^{N} \alpha_i y_i \mathbf{x}_i \right)^T \left( \sum_{j=1}^{N} \alpha_j y_j \mathbf{x}_j \right) \\
&= \sum_{i=1}^{N} \sum_{j=1}^{N} \alpha_i \alpha_j y_i y_j \mathbf{x}_i^T \mathbf{x}_j \\

\mathcal{L}_P &= \frac{1}{2} \sum_{i=1}^{N} \sum_{j=1}^{N} \alpha_i \alpha_j y_i y_j \mathbf{x}_i^T \mathbf{x}_j - \sum_{i=1}^{N} \alpha_i y_i \left( \mathbf{w}^T \mathbf{x}_i + w_0 \right) + \sum_{i=1}^{N} \alpha_i \\
&= \frac{1}{2} \sum_{i=1}^{N} \sum_{j=1}^{N} \alpha_i \alpha_j y_i y_j \mathbf{x}_i^T \mathbf{x}_j - \sum_{i=1}^{N} \alpha_i y_i \mathbf{w}^T \mathbf{x}_i - w_0 \sum_{i=1}^{N} \alpha_i y_i + \sum_{i=1}^{N} \alpha_i \\
&= \sum_{i=1}^{N} \alpha_i - \frac{1}{2} \sum_{i=1}^{N} \sum_{j=1}^{N} \alpha_i \alpha_j y_i y_j \mathbf{x}_i^T \mathbf{x}_j \quad \text{(since $\sum_{i=1}^{N} \alpha_i y_i = 0$ and $\mathbf{w} = \sum_{i=1}^{N} \alpha_i y_i \mathbf{x}_i$)} \\

\text{Dual problem:} & \\
\text{Maximize} & \quad \sum_{i=1}^{N} \alpha_i - \frac{1}{2} \sum_{i=1}^{N} \sum_{j=1}^{N} \alpha_i \alpha_j y_i y_j \mathbf{x}_i^T \mathbf{x}_j \\
\text{Subject to:} & \\
& \sum_{i=1}^{N} \alpha_i y_i = 0 \\
& \alpha_i \geq 0 \quad \forall i \\ 
\text{Decision Variables:}
& \set{\alpha_1, \alpha_2, ... ,\alpha_N}
\end{aligned}
$$
### Complexity:
In this formulation the upper bound for time complexity is $O(N^3)$, and the upper bound for space complexity is $O(N^2)$.
### Critical Aspects
Once we solve for $\alpha^t$, we see that though there are $N$ of them, most vanish with $\alpha^t=0$ and only a small percentage have $\alpha^t>0$. The set of $x^t$ whose $\alpha^t>0$ are the **support vectors**, and as we can see in equation 10.50, $\textbf{w}$ is written as the weighted sum of these training instances that are selected as the support vectors. These are the $\textbf{x}^t$, which satisfy 
$r^t (\mathbf{w}^T x^t + w_0) = 1$.
Meaning these points lie on the margin, We can use this fact to calculate $w_0$ from any support vector as 
$w_0 = r^t - \mathbf{w}^T x^t$.

For numerical stability, it is advised that this is done for all support vectors and an average is taken. The dicriminant thus found is called the **support vector machine (SVM)**.

**Sum of Lagrange Multipliers Condition**: This condition $\sum_{i=1}^{N} \alpha_i y_i = 0$ is significant because it reflects the balance between the support vectors on the margin of each class. This equation ensures that the solution to the dual problem satisfies the constraint that the decision boundary must separate the classes. The support vectors from each class "pull" the decision boundary in opposite directions, and this equation ensures that the net "pull" is zero, meaning the boundary is optimally positioned between classes.

# The model
Assume the solution $\rightarrow \alpha^*$
$$
\begin{aligned}
g(\mathbf{x}) = \mathbf{w}^T \mathbf{x} + w_0 & =  \left[ \sum_{i=1}^N \alpha_i^* y_i \mathbf{x}_i \right]^T \mathbf{x} + w_0 \\
& =\sum_{i=1}^N \alpha_i^* y_i \mathbf{x}_i^T \mathbf{x} + w_0
\end{aligned}
$$
This model only depends on support vectors since $\alpha^*$.

# Nonseperable Case
We introduce slack variable $\xi_i$

$$
\begin{align*}
& \text{minimize} \quad \frac{1}{2} \|\mathbf{w}\|^2 + C \sum_{i=1}^N \xi_i \\
& \text{subject to:} \\
& \quad y_i(\mathbf{w}^T \mathbf{x}_i + w_0) \geq 1 - \xi_i, \quad \forall i \\
& \quad \alpha_i \; [ \; \xi_i \geq 0 \quad \forall i \\
& \quad \beta_i \; [ \; \xi_i \ge 0 \quad \forall i \\
\end{align*}
$$
## Langrangian Formulation With Slack Variable
$$
\mathcal{L}_P = \frac{1}{2} \mathbf{w}^T \mathbf{w} + C \sum_{i=1}^N \xi_i - \sum_{i=1}^N \alpha_i [ y_i(\mathbf{w}^T \mathbf{x}_i + w_0) - 1 + \xi_i ] - \sum_{i=1}^N \beta_i \xi_i
$$
Note that $\beta_i$ comes from the second constraints, we use a second langrangian formula for the slack variable and therefore have to use this value.
## Derivatives

$$
\begin{align*}
\frac{\partial \mathcal{L}_P}{\partial \mathbf{w}} &= \mathbf{w} - \sum_{i=1}^N \alpha_i y_i \mathbf{x}_i = 0 &\Rightarrow \mathbf{w} = \sum_{i=1}^N \alpha_i y_i \mathbf{x}_i \\
\frac{\partial \mathcal{L}_P}{\partial w_0} &= -\sum_{i=1}^N \alpha_i y_i = 0 &\Rightarrow \sum_{i=1}^N \alpha_i y_i = 0 \\
\frac{\partial \mathcal{L}_P}{\partial \xi_i} &= C - \alpha_i - \beta_i = 0 &\Rightarrow \alpha_i + \beta_i = C \quad \forall i \\
&& \alpha_i \geq 0, \quad \beta_i \geq 0 \\
&& 0 \leq \alpha_i \leq C \quad \forall i
\end{align*}
$$

[[Kernel Functions]]

# Matrix Representation
$$
W(\alpha) = \alpha^T1-\frac{1}{2}\alpha^TH\alpha
$$
$$
\sum_{i=1}^{N} \sum_{j=1}^{N} \alpha_i \alpha_j y_i y_j \ k( x_i, x_j ) = \alpha^T ((yy^T) \circ K) \alpha
$$
Note that the $\circ$ here represents a pairwise multiplication.

## Validity Of A Kernel
If k is a valid kernel its matrix should be **psd** (positive semi-definite) matrix.
$$
\alpha^T.K,\alpha \ge 0 \ \ \ \ \forall \alpha \in \mathbb{R}^N
$$
OR
$$
\begin{align}
K=XX^T \\
a^T K a \geq 0 \\
a^T XX^T a \geq 0 \\
(X^T a)^T X^T a \geq 0 \\
\| X^T a \|_2^2 \geq 0
\end{align}
$$
