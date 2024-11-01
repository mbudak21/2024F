import matplotlib.pyplot as plt
import numpy as np


# read data into memory
data_set_train = np.genfromtxt("hw04_data_set_train.csv", delimiter = ",", skip_header = 1)
data_set_test = np.genfromtxt("hw04_data_set_test.csv", delimiter = ",", skip_header = 1)

# get x and y values
X_train = data_set_train[:, 0:1]
y_train = data_set_train[:, 1]
X_test = data_set_test[:, 0:1]
y_test = data_set_test[:, 1]

# set drawing parameters
minimum_value = 1.5
maximum_value = 5.1
step_size = 0.001
X_interval = np.arange(start = minimum_value, stop = maximum_value + step_size, step = step_size)
X_interval = X_interval.reshape(len(X_interval), 1)

def plot_figure(X_train, y_train, X_test, y_test, X_interval, y_interval_hat):
    fig = plt.figure(figsize = (8, 4))
    plt.plot(X_train[:, 0], y_train, "b.", markersize = 10)
    plt.plot(X_test[:, 0], y_test, "r.", markersize = 10)
    plt.plot(X_interval[:, 0], y_interval_hat, "k-")
    plt.xlabel("Eruption time (min)")
    plt.ylabel("Waiting time to next eruption (min)")
    plt.legend(["training", "test"])
    plt.show()
    return(fig)

# STEP 2
# should return necessary data structures for trained tree
def decision_tree_regression_train(X_train, y_train, P):
    # create necessary data structures
    node_indices = {}
    is_terminal = {}
    need_split = {}


    node_features = {}
    node_splits = {}
    node_means = {} # Instead of frequencies, we store the mean of y values in each node
    # your implementation starts below

    # Initialization
    node_indices = {0: np.arange(X_train.shape[0])}
    is_terminal = {0: False}
    need_split = {0: True}

    while True:
        split_nodes = [node for node, need in need_split.items() if need]
        if not split_nodes:
            break

        for node in split_nodes:
            data_indices = node_indices[node]
            if len(data_indices) <= P:
                is_terminal[node] = True
                need_split[node] = False
                node_means[node] = np.mean(y_train[data_indices]) if data_indices.size > 0 else 0
                continue

            best_feature, best_split, min_mse = None, None, float("inf")
            for feature in range(X_train.shape[1]):
                unique_splits = np.unique(X_train[data_indices, feature])
                for split in unique_splits:
                    left_indices = data_indices[X_train[data_indices, feature] < split]
                    right_indices = data_indices[X_train[data_indices, feature] >= split]
                    
                    # Only attempt to split if both left and right have more than zero elements
                    if len(left_indices) > 0 and len(right_indices) > 0:
                        left_mean = np.mean(y_train[left_indices])
                        right_mean = np.mean(y_train[right_indices])
                        
                        left_mse = np.mean((y_train[left_indices] - left_mean) ** 2)
                        right_mse = np.mean((y_train[right_indices] - right_mean) ** 2)
                        
                        mse = (len(left_indices) * left_mse + len(right_indices) * right_mse) / len(data_indices)
                        
                        if mse < min_mse:
                            min_mse = mse
                            best_feature = feature
                            best_split = split
                unique_splits = np.unique(X_train[data_indices, feature])
                for split in unique_splits:
                    left_indices = data_indices[X_train[data_indices, feature] < split]
                    right_indices = data_indices[X_train[data_indices, feature] >= split]


            # Correcting node indexing
            if best_feature is not None:
                left_node = 2 * node + 1
                right_node = 2 * node + 2

                left_indices = data_indices[X_train[data_indices, best_feature] < best_split]
                right_indices = data_indices[X_train[data_indices, best_feature] >= best_split]

                node_indices[left_node] = left_indices
                node_indices[right_node] = right_indices
                is_terminal[node] = False
                need_split[node] = False
                is_terminal[left_node] = False
                need_split[left_node] = True
                is_terminal[right_node] = False
                need_split[right_node] = True
                node_features[node] = best_feature
                node_splits[node] = best_split
                # Removing the line that sets node_means[node] here, as it's redundant
            else:
                is_terminal[node] = True
                need_split[node] = False
                node_means[node] = np.mean(y_train[data_indices]) if data_indices.size > 0 else 0

    # your implementation ends above
    return(is_terminal, node_features, node_splits, node_means)

# STEP 3
# assuming that there are N query data points
# should return a numpy array with shape (N,)
def decision_tree_regression_test(X_query, is_terminal, node_features, node_splits, node_means):
    # your implementation starts below

    def decision_tree_get_y_hat(x, is_terminal, node_features, node_splits, node_means):
        node = 0
        while True:  # previously was: while not is_terminal[node]:
            if node not in is_terminal or is_terminal[node]:
                # If we reach a non-existent or terminal node, return the mean
                return node_means.get(node, 0)  # Use a default value if node is not in node_means

            split = node_splits[node]
            if x[node_features[node]] < split:
                node = 2 * node + 1  # Go to left child
            else:
                node = 2 * node + 2  # Go to right child


    y_hat = np.zeros(X_query.shape[0])
    for i, x in enumerate(X_query):
        y_hat[i] = decision_tree_get_y_hat(x, is_terminal, node_features, node_splits, node_means)
    # your implementation ends above
    return(y_hat)

# STEP 4
# assuming that there are T terminal node
# should print T rule sets as described
def extract_rule_sets(is_terminal, node_features, node_splits, node_means):
    # your implementation starts below
    def traverse(node, path):
        if is_terminal[node]:
            # Format the conditions as specified
            conditions = [f"x{feature + 1} {'>' if '>=' in cond else '<='} {cond.split(' ')[-1]}" for feature, cond in enumerate(path)]
            print(f"Node {node:02d}: [{' '.join(conditions)}] => {node_means[node]}")
            return
        feature = node_features[node]
        split = node_splits[node]
        # Modify the condition strings to include the split
        traverse(2 * node + 1, path + [f"Feature {feature} < {split}"])
        traverse(2 * node + 2, path + [f"Feature {feature} >= {split}"])

    traverse(0, [])
    # your implementation ends above

P = 20
is_terminal, node_features, node_splits, node_means = decision_tree_regression_train(X_train, y_train, P)
y_interval_hat = decision_tree_regression_test(X_interval, is_terminal, node_features, node_splits, node_means)
fig = plot_figure(X_train, y_train, X_test, y_test, X_interval, y_interval_hat)
fig.savefig("decision_tree_regression_{}.pdf".format(P), bbox_inches = "tight")

y_train_hat = decision_tree_regression_test(X_train, is_terminal, node_features, node_splits, node_means)
rmse = np.sqrt(np.mean((y_train - y_train_hat)**2))
print("RMSE on training set is {} when P is {}".format(rmse, P))

y_test_hat = decision_tree_regression_test(X_test, is_terminal, node_features, node_splits, node_means)
rmse = np.sqrt(np.mean((y_test - y_test_hat)**2))
print("RMSE on test set is {} when P is {}".format(rmse, P))

P = 50
is_terminal, node_features, node_splits, node_means = decision_tree_regression_train(X_train, y_train, P)
y_interval_hat = decision_tree_regression_test(X_interval, is_terminal, node_features, node_splits, node_means)
fig = plot_figure(X_train, y_train, X_test, y_test, X_interval, y_interval_hat)
fig.savefig("decision_tree_regression_{}.pdf".format(P), bbox_inches = "tight")

y_train_hat = decision_tree_regression_test(X_train, is_terminal, node_features, node_splits, node_means)
rmse = np.sqrt(np.mean((y_train - y_train_hat)**2))
print("RMSE on training set is {} when P is {}".format(rmse, P))

y_test_hat = decision_tree_regression_test(X_test, is_terminal, node_features, node_splits, node_means)
rmse = np.sqrt(np.mean((y_test - y_test_hat)**2))
print("RMSE on test set is {} when P is {}".format(rmse, P))

extract_rule_sets(is_terminal, node_features, node_splits, node_means)
