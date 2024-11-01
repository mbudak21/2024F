A way to find the probability of a hypothesis given observed evidence. In machine learning, it's often used for classification tasks.

$$
P(H|E) = \frac{P(E|H)P(H)}{P(E)}
$$

Where:
- $P(H|E):$ **Posterior** probability
	the probability of the hypothesis H given the evidence E.
- $P(E|H):$ **Likelihood** 
	the probability of observing the evidence E given that the hypothesis H is true.
- $P(H):$ **Prior** probability
	the initial probability of the hypothesis H before observing any evidence.
- $P(E):$ **Evidence**
	the total probability of observing the evidence E under all possible hypotheses.