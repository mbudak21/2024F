It is one of the [[non-Parametric Methods]] and can be used for both [[Regression]] and [[Classification]]. Is usually a part of [[Supervised Learning]].


## Impurity
$$I_m(\text{NodeA}) = -\sum_{c=1}^{K}{P_{mc}.log_2(P_{mc})}$$
## Information Gain
$$
= I(ParentNode) - I(split)
$$


## Measures Of Impurity
### 1. Entropy
$$
\text{Entropy}=−p⋅log2_​(p)−(1−p)⋅log_2​(1−p)
$$

### 2. Gini Index
Univariate:

$$
\text{Gini Index}=2⋅p⋅(1−p)
$$
Multivariate:
$$
\text{Gini Index}=\sum_{i=1}^{C}{p_i}​⋅(1−p_i​)
$$

### 3. Misclassification Error
For binary classification:

Misclassification Error=1−max⁡(p,1−p)Misclassification Error=1−max(p,1−p)

For multi-class classification:

Misclassification Error=1−max⁡(p1,p2,…,pK)Misclassification Error=1−max(p1​,p2​,…,pK​)