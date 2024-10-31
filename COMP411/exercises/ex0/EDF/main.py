import numpy as np
import matplotlib.pyplot as plt

"""read train and test data"""
train_data = np.load('data/train_data.npy')
train_labels = np.load('data/train_labels.npy')
test_data = np.load('data/test_data.npy')
test_labels = np.load('data/test_labels.npy')


"""visualize train data"""
plt.scatter(train_data[:,0],train_data[:,1], c=train_labels)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Train Data")
plt.show()
plt.clf()

import edf


"""we manually set the number of input features (2)
and number of classes (1) which will be used to
define the model"""

nInputs = 2
nLabels = 1

"""below, MLPparams is an EDF ParameterPackage whose
purpose is to define and store the parameters of the model,
while MLPgraph is a function that implements the model's
forward pass -- in this case, just a linear layer followed by sigmoid activation"""

class MLPparams(edf.ParameterPackage):
    def __init__(self,nInputs, nLabels):
        self.layer = edf.AffineParams(nInputs, nLabels)
        
def MLPsigmoidgraph(Phi, x):
    return edf.Sigmoid(edf.Affine(Phi.layer, x))


"""we then construct our model"""

np.random.seed(42)
edf.clear_compgraph()
xnode = edf.Input()
ynode = edf.Input()

Phi = MLPparams(nInputs, nLabels)
probnode = MLPsigmoidgraph(Phi, xnode)
lossnode = edf.BCELoss(probnode, ynode)



"""the following function is used to train and test the model
   by passing lossnode to the function, we enable training"""

def run_one_epoch(data, labels, xnode, ynode, probnode, lossnode=None):
    xnode.value = data
    ynode.value = labels
    edf.Forward()
    errors = np.sum(np.not_equal(probnode.value > 0.5, ynode.value))
    if lossnode:
        edf.Backward(lossnode)
        edf.SGD()
    return 100 * errors / len(data)


train_errors = []
test_errors = []
num_epochs = 10
edf.learning_rate = 0.5

for epoch in range(num_epochs):
    train_error = run_one_epoch(train_data, train_labels, xnode, ynode, probnode, lossnode) #pass lossnode to enable training
    test_error = run_one_epoch(test_data, test_labels, xnode, ynode, probnode) #don't pass lossnode to disable training
    train_errors.append(train_error)
    test_errors.append(test_error)
    print(f'Epoch {epoch:02d}: train error {train_error:.3f}%, test error {test_error:.3f}%')


"""we can then plot the error per epoch on the training and test data"""

plt.xlabel("epochs")
plt.ylabel("error (%)")
plt.plot(np.arange(len(test_errors)), test_errors, color='red')
plt.plot(np.arange(len(train_errors)), train_errors, color='blue')
plt.legend(['test error', 'train error'], loc='upper right')
plt.savefig('error_metrics.png')
plt.show()
plt.clf()
