
Parametric classification uses a parametric function in the bayesian estimator to find proper class probabilities: $Pr(y=c|x)$. The score function, $g_c(x)$ is usually chosen to be the Logarithm of the $Pr(y=c|x)$ without the evidence in the denominator, $P(x)$. 

## Parametric vs non-Parametric classification
The main difference lies in the $P(x|y=c)$ function, in parametric classification we use parametric methods (we assume a distribution), whereas in the non-parametric classification we use non-parametric methods such as KNN, Parzen Windows, and so on. 

Related: [[non-Parametric Classification]], [[non-Parametric Methods]]



![[Pasted image 20231107223759.png]]  

$g_c:$ [[Score function]] for class $c$

$$
g_c(x)=log.Pr(y=c|x)
$$




