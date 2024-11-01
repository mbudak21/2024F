We assume that the sample $X = \set{x^t}_{t=1}^{N}$ is independently drawn from some unknown probability density $p( \ . )$. And we estimate $p( \ . )$ with $\hat{p}( \ . )$.

## Histogram Estimator
We need to choose h and a starting point.
$$
\hat{p}(x) = \frac{ \# \set{x^t \text{in the same bin as } \cal{X}}}{Nh}
$$
![[Pasted image 20231216144143.png|525]]
### Regression Version
$$
\begin{align}
& \hat{g}(x) = \frac{\sum_{t=1}^{N} b(x, x^t) r^t}{\sum_{t=1}^{N} b(x, x^t)} \\

& \text{where} \ \ \

b(x, x^t) = \begin{cases} 
1 & \text{if } x^t \text{ is the same bin with } x \\
0 & \text{otherwise}
\end{cases}
\end{align}
$$
![[Pasted image 20231220111456.png|525]]
## Naive Estimator
No need to set a starting point $x_0$
$$
\hat{p}(x) = \frac{ \# \set{x-h<x^t\le x+h}}{2Nh}
$$

![[Pasted image 20231216162016.png|525]]
**The Estimator Can Also Be Written As:**
$$
\hat{p}(x)=\frac{1}{Nh}\sum^{N}_{t=1}{w\left( \frac{x-x^t}{h} \right)}   
$$
With the weight function defined as:
$$
w(u) = 
\begin{cases} 
\frac{1}{2} & \text{if } |u| < 1 \\
0 & \text{otherwise} 
\end{cases}
$$
## Kernel Estimator
To get a smooth estimate, we need to use a smooth weight function, called a *kernel function*. Most popular one being the **Gaussian Kernel:**
$$
K(u) = \frac{1}{\sqrt{2\pi}} \exp\left[ -\frac{u^2}{2} \right]

$$
Where $K(u)$ is just $N\textasciitilde(u; \mu=0, \sigma^2=1)$


The *kernel estimator*, also called **Parzen windows**, is defined as:
$$
\hat{p}(x) = \frac{1}{Nh} \sum_{t=1}^{N} K\left( \frac{x - x^t}{h} \right)
$$
## K-Nearest Neighbor Estimator (KNN)

$$
\hat{p}(x) = \frac{k}{N \ 2d_k(x)}
$$
where $d_k(x):$ The distance to the $k \ \text{th}$ neighbor.