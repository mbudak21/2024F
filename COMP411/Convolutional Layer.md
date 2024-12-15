The convolution operation in a convolutional layer involves sliding a small window (called a [kernel](https://en.wikipedia.org/wiki/Kernel_(image_processing) "Kernel (image processing)") or filter) across the input data and computing the [dot product](https://en.wikipedia.org/wiki/Dot_product "Dot product") between the values in the kernel and the input at each position. This process creates a feature map that represents detected [features](https://en.wikipedia.org/wiki/Feature_(computer_vision) "Feature (computer vision)") in the input

## Concepts

### Kernel

**Kernels**, also known as **filters**, are small matrices of weights that are learned during the training process. Each kernel is responsible for detecting a specific feature in the input data. The size of the kernel is a hyperparameter that affects the network's behavior.

### Convolution
Commonly used convolutions are 1D (for audio and text), 2D (for images), and 3D (for spatial objects, and videos).

### Stride
Stride determines how the kernel moves across the input data. A stride of 1 means the kernel shifts by one pixel at a time, while a larger stride (e.g., 2 or 3) results in less overlap between convolutions and produces smaller output feature maps.

### Padding
Padding involves adding extra pixels around the edges of the input data. It serves two main purposes:

- Preserving spatial dimensions: Without padding, each convolution reduces the size of the feature map.
- Handling border pixels: Padding ensures that border pixels are given equal importance in the convolution process.

Common padding strategies include:

- No padding/valid padding. This strategy typically causes the output to shrink.
- Same padding: Any method that ensures the output size same as input size is a same padding strategy.
- Full padding: Any method that ensures each input entry is convolved over for the same number of times is a full padding strategy.

Common padding algorithms include:

- Zero padding: Add zero entries to the borders of input.
- Mirror/reflect/symmetric padding: Reflect the input array on the border.
- Circular padding: Cycle the input array back to the opposite border, like a torus.

The exact numbers used in convolutions is complicated, for which we refer to (Dumoulin and Visin, 2018)[[3]](https://en.wikipedia.org/wiki/Convolutional_layer#cite_note-3) for details.