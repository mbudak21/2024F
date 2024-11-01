In linear regression the model family is the family of lines. 
Backlinks to: [[Regression]]

## Matrix Version
$$
f(\mathbf{x}, \mathbf{w}) = \mathbf{w}^T \mathbf{x}
$$
$$
E(\mathbf{w}) = \sum_{i=1}^{N} \left( f(\mathbf{x}_i, \mathbf{w}) - y_i \right)^2
$$
$$
= \sum_{i=1}^{N} \left( \mathbf{x}_i^T \mathbf{w} - y_i \right)^2

= \| \mathbf{X} \mathbf{w} - \mathbf{y} \|_2^2
$$





## ?

Squared Error:
$$
\sum_{i=1}^{N}{(y_i-\hat{y}_i)^2} = \sum_{i=1}^{N}{e_i^2}
$$

We want to minimize the following error metric, with respect to $w_1$ and $w_0$ :
$$
\sum_{i=1}^{N}{(y_i-(w_1x_{i1}+w_0))^2}
$$

To find the minimal point, we set the derivative to 0:
$$
\frac{dError}{dw_0} = \sum_{i=1}^{N}{\frac{d(y_i-(w_1x_{i1} + w_0))^2}{dw_0}} = 0
$$

$$
\sum_{i=1}^{N}{2(y_i-(w_1x_{i1}+w_0))(-1) = 0} 
$$
----

$$
\frac{dError}{dw_1} = \sum_{i=1}^{N}{\frac{d(y_i-(w_1x_{i1} + w_0))^2}{dw_1}} = 0
$$
$$
\sum_{i=1}^{N}{2(y_i-(w_1x_{i1}+w_0))(-x_{i1}) = 0} 

$$
----

Solve for $w_1$ and $w_0$ 