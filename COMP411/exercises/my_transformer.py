import numpy as np

# Define dataset
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]])
Y = np.array([0, 1, 1, 0])

class neuron:
    def __init__(self, num_inputs):
        self.w = np.random.randn(num_inputs)  # One weight per input
        self.b = np.random.randn()

    def forward(self, inputs):
        z = np.dot(inputs, self.w) + self.b
        return np.minimum(0, z)


input_layer = [neuron(1), neuron(1)]
hidden_layer = [neuron(2), neuron(2)]
output_layer = [neuron(2)]

model = [input_layer, hidden_layer, output_layer]

sample_in = X[0]
hidden_out = [neuron.forward(sample_in) for neuron in hidden_layer]
output = output_layer[0].forward(hidden_out)

print("Model Structure:", model)
print("Sample Forward Pass Output:", output)

import plotly.graph_objects as go

def visualize_nn_interactive(model):
    fig = go.Figure()

    # Add each node layer with 3D positioning and interactive properties
    for i, layer in enumerate(model):
        for j, neuron in enumerate(layer):
            fig.add_trace(go.Scatter3d(
                x=[i], y=[j], z=[0],
                mode='markers+text',
                marker=dict(size=12, color='blue'),
                text=f"Layer {i}, Neuron {j+1}",
                textposition="bottom center"
            ))

    fig.update_layout(scene=dict(
        xaxis=dict(title="Layers"),
        yaxis=dict(title="Neurons"),
        zaxis=dict(title="Activation Level")
    ))

    fig.show()

visualize_nn_interactive(model)

