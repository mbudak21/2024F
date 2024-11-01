## Maximum Likelihood Estimation (MLE)
MLE is a special case of density estimation where we aim to find the parameters $\theta$ that maximize the [[likelihood]] function $l(\theta)$. The likelihood function represents the likelihood of the observed data $X$ given the parameters $\theta$.

$$l(\theta)=p(X|\theta)=\prod_{i=0}^{N}{p(x_i|\theta)}$$

MLE estimates $\theta$ by maximizing this function, i.e., we find the value of $\theta$ that makes the observed data most probable.

### Gaussian Distribution
#### How to find $\mu$ and $\sigma^2$? 
**Note:** The derivations here come from setting the derivative of the likelihood to zero, aka, finding the $\theta$ that maximizes likelihood.
$$
\mu_{MLE} = \text{simply the average of the points}
$$
$$
\sigma^2_{\text{MLE}} = \frac{1}{n} \sum_{i=1}^{n} (x_i - \mu)^2
$$
$\sigma^2:$ The average of mean diff squared