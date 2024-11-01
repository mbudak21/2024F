Bayes Theorem:
$$
Pr(y=c|x) = \frac{p(x|y=c)Pr(y=c)}{p(x)}
$$

Where:
- $Pr(y=c|x):$ **Posterior Probability**
- $p(x|y=c):$ **Likelihood**
	Is the pdf of class $c$. Assuming class $c$ is the correct one, what is the probability of point $x$ being on class $c$?
- $Pr(y=c):$ **Prior**
	Prior of class $c$, frequency of class $c$
- $p(x):$ **Evidence**
	A normalizing constant which is not needed for the scoring functions. The evidence $p(x)$ is the probability of observing the data $x$ under all possible hypotheses weighted by their probabilities. So: $\sum_{c=1}^{K}{p(x|y=c)Pr(y=c)}$


