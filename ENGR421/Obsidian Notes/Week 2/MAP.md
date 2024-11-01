### Maximum A Posteriori (MAP)
MAP goes one step further by incorporating prior beliefs or information $p(\theta)$ about the parameters $\theta$. It estimates the parameters $\theta$ by maximizing the posterior density function, which is calculated using [[Bayes' Rule]]:

$$
p(\theta|X) = \frac{p(X|\theta)\ \\p(\theta)}{p(X)}
$$

Here:
- $P(\theta|X):$ **Posterior**
- $p(X|\theta):$ **Likelihood**
- $P(\theta):$ **Prior**
- $P(X):$ **Evidence**

Here  $p(X)$ is the evidence (a normalizing constant). MAP estimates are a compromise between the **prior information** and the **likelihood** of the data.
