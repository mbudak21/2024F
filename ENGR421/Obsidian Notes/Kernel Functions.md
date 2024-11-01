Each kernel has a different way of computing the similarity between two data points. Here's a breakdown of the kernels:
![[Pasted image 20231219144604.png|575]]

1. **Linear Kernel**: The simplest kernel, computed as the dot product of two vectors $x_i$​ and $x_j$​. This kernel implies that the data is already linearly separable in the input feature space. $$k(x_i, x_j) = x_i^T x_j$$
    
2. **Polynomial Kernel**: Introduces non-linearity and can model more complex relationships. It's computed as $\left( \langle x_i, x_j \rangle + r \right)^d$, where $r$ is typically set to $1$ (as seen in the image), and $d$ is the degree of the polynomial. $$k(x_i, x_j) = (\langle x_i, x_j \rangle + 1)^d$$
    
3. **Sigmoidal Kernel**: Similar to the activation function used in neural networks, the sigmoid kernel is computed as $\tanh(\gamma \langle x_i, x_j \rangle + r)$, where $\gamma$ is a scale factor and $r$ is the additive term. $$k(x_i, x_j) = \tanh(\gamma \langle x_i, x_j \rangle + r)$$
    
4. **Gaussian (RBF) Kernel**: Computes the similarity based on the distance between points in a high-dimensional space, and can handle complex, non-linear data separations. It's given by $\exp\left(-\frac{\|x_i - x_j\|^2}{2\sigma^2}\right)$, where $\sigma$ is the standard deviation or bandwidth of the Gaussian distribution. $$k(x_i, x_j) = \exp\left(-\frac{\|x_i - x_j\|^2}{2\sigma^2}\right)$$
    

Each kernel has parameters that need to be tuned, such as dd and rr for the polynomial kernel or σσ for the Gaussian kernel. The choice of kernel and its parameters can significantly affect the SVM's performance.