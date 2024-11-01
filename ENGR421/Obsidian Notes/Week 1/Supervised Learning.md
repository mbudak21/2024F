**1) Definiton:**

$X = {(x_i, y_i)}^{N}_{i=1}\ \ \ \ y_i \in R$ , where $y_i$ represents the target variable which can be either continious([[Regression]]) or categorical ([[Classification]]).

**2) Goal:**

We aim to minimize the [[Error Function]], which is defined as such:
$$
E(\theta|X) = \sum_{i=1}^{N}{L(y^i, g(x^i|\theta))}
$$
Where,
$E(.)$ is the [[Error Function]]
$L(.)$ is the [[Loss Function]]
$g(.)$ denotes our [[Hypothesis class]], and
$g(.|\theta)$ Specific model in the Hyptohesis Class denoted by parameters $\theta$ 

**3) Optimization Procedure:** 
We aim to find $\theta^*$ that minimizes the approximation error.
$$
\theta^* = arg \underset{\theta}{\mathrm{min}}\ E(\theta|X)
$$



$\mathcal{H}:$ [[Hypothesis class]], denotes all possible parameters of a given model, which is set by the expert. 

**Version Space**: Set of all $h \in \mathcal{H}$ that are correct for the training dataset.
 
Supervised learning is classified into two categories of algorithms, depending on the data wanted. The data is either *Classified* to a class, or *guessed* to a real number. [[Classification]] and [[Regression]]

