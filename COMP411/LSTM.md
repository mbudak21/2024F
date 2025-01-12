
# Principle
An LSTM unit is typically composed of a **cell** and three gates: an **input gate**, an **output gate**, and a **forget gate**. The cell remembers values over arbitrary time intervals, and the gates regulate the flow of information into and out of the cell. Forget gates decide what information to discard from the previous state, by mapping the previous state and the current input to a value between 0 and 1. A (rounded) value of 1 signifies retention of the information, and a value of 0 represents discarding. Input gates decide which pieces of new information to store in the current cell state, using the same system as forget gates. Output gates control which pieces of information in the current cell state to output, by assigning a value from 0 to 1 to the information, considering the previous and current states.

# Inner Workings

![[Pasted image 20250108180140.png]]

![[Pasted image 20250108181215.png]]
$f_t$: Forget Gate
	Looks at $h_{t-1}$ and $x_t$ and outputs a number in [0..1] for each number in the cell state. The result is later multiplied with the Long-Term memory, hence, the `forget` mechanism.
$$
f_t = \sigma \left( W_f \cdot \begin{bmatrix} h_{t-1} \\ x_t \end{bmatrix} + b_f \right)
$$
![[Pasted image 20250108181252.png]]
$$
\begin{align*}
i_t &= \sigma \left( W_i \cdot \begin{bmatrix} h_{t-1} \\ x_t \end{bmatrix} + b_i \right) \\
\tilde{C}_t &= \tanh \left( W_C \cdot \begin{bmatrix} h_{t-1} \\ x_t \end{bmatrix} + b_C \right)
\end{align*}
$$
![[Pasted image 20250108181440.png]]
$$
C_t = f_t \ast C_{t-1} + i_t \ast \tilde{C}_t
$$

![[Pasted image 20250108181607.png]]
$$
\begin{align*}
o_t &= \sigma \left( W_o \cdot \begin{bmatrix} h_{t-1} \\ x_t \end{bmatrix} + b_o \right) \\
h_t &= o_t \ast \tanh(C_t)
\end{align*}
$$





$$
\begin{align*}
f_t &= \sigma_g(W_f x_t + U_f h_{t-1} + b_f) \\
i_t &= \sigma_g(W_i x_t + U_i h_{t-1} + b_i) \\
o_t &= \sigma_g(W_o x_t + U_o h_{t-1} + b_o) \\
\tilde{c}_t &= \sigma_c(W_c x_t + U_c h_{t-1} + b_c) \\
c_t &= f_t \odot c_{t-1} + i_t \odot \tilde{c}_t \\
h_t &= o_t \odot \sigma_h(c_t)
\end{align*}
$$











$$
\begin{align*}
f_t &= \sigma(W_{if} x_t + b_f + W_{hf} h_{t-1} + b_{hf}) \\
i_t &= \sigma(W_{ii} x_t + b_{ii} + W_{hi} h_{t-1} + b_{hi}) \\
o_t &= \sigma(W_{io} x_t + b_{io} + W_{ho} h_{t-1} + b_{ho}) \\
g_t &= \tanh(W_{ig} x_t + b_{ig} + W_{hg} h_{t-1} + b_{hg}) \\
c_t &= f_t \odot c_{t-1} + i_t \odot g_t \\
h_t &= o_t \odot \tanh(c_t)
\end{align*}
$$



