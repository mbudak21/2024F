Recurrent Neural Networks, process data across multiple time steps. Here is a RNN as a function:
$$
f_{\theta} \ (x_t, h_t) \mapsto (y_t, h_{t+1})
$$

The hidden state is updated as follows:
$$
h_t = f(W_h h_{t-1} + W_x x_t + b)
$$

Where:  
- $f$: Non-linear activation function (e.g., tanh or ReLU).
- $W_h$: Weights for the hidden state.  
- $W_x$: Weights for the input.  
- $b$: Bias term.  



The building block of RNNs is the [[Recurrent Unit]]. This unit maintains a hidden state, essentially a form of memory, which is updated at each time step based on the current input and the previous hidden state. This feedback loop allows the network to learn from past inputs, and incorporate that knowledge into its current processing.

Early RNNs suffered from the [vanishing gradient problem](https://en.wikipedia.org/wiki/Vanishing_gradient_problem "Vanishing gradient problem"), limiting their ability to learn long-range dependencies. This was solved by the [long short-term memory](https://en.wikipedia.org/wiki/Long_short-term_memory "Long short-term memory") (LSTM) variant in 1997, thus making it the standard architecture for RNN.

