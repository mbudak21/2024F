# Semantics

BayesNet = Graph Topology + CPTs
*CPT:* conditional probability distribution
- Each node has a **conditional probability distribution (CPT)** associated with it.
- The probability of a node $X_i$ is conditioned on its parent nodes: $P(X_i | Parents(X_i))$.

![[Pasted image 20241226135259.png]]
$P(-t, +r) = P(-t|+r)P(+r) = \frac{1}{4}*\frac{1}{4}$
