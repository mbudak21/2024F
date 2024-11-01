import numpy as np
import pandas as pd



X = np.genfromtxt("hw01_data_points.csv", delimiter = ",", dtype = str)
y = np.genfromtxt("hw01_class_labels.csv", delimiter = ",", dtype = int)



# STEP 3
# first 50000 data points should be included to train
# remaining 44727 data points should be included to test
# should return X_train, y_train, X_test, and y_test
def train_test_split(X, y):
    # your implementation starts below
    trainset_size = 50000
    X_train = X[:50000]
    X_test = X[50000:]

    y_train = y[:50000]
    y_test = y[50000:]
    # your implementation ends above
    return(X_train, y_train, X_test, y_test)

X_train, y_train, X_test, y_test = train_test_split(X, y)
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)



# STEP 4
# assuming that there are K classes
# should return a numpy array with shape (K,)
def estimate_prior_probabilities(y):
    # your implementation starts below
        
    # Assume class numeration starts from 1
    K = max(y) # Number of classes
    size = y.shape[0] # Total size of set y
    class_priors = []

    for c in range(1, K): # From 1 to K-1
        class_priors.append(sum(y==c)/size)

    class_priors.append(1-sum(class_priors))
    
    # your implementation ends above
    return(class_priors)

class_priors = estimate_prior_probabilities(y_train)
print(class_priors)



# STEP 5
# assuming that there are K classes and D features
# should return four numpy arrays with shape (K, D)
def estimate_nucleotide_probabilities(X, y):
    # your implementation starts below
    K = max(y)  # Number of classes (assuming y starts from 0)
    D = X.shape[1]  # Number of features
    
    pAcd = np.zeros((K, D))
    pCcd = np.zeros((K, D))
    pGcd = np.zeros((K, D))
    pTcd = np.zeros((K, D))
    
    for c in range(1, K+1):
        # Filter data by class
        X_c = X[y == c]
        
        for d in range(D):
            feature_column = X_c[:, d]
            total_samples = len(feature_column)
            
            pAcd[c-1][d] = np.sum(feature_column == 'A') / total_samples
            pCcd[c-1][d] = np.sum(feature_column == 'C') / total_samples
            pGcd[c-1][d] = np.sum(feature_column == 'G') / total_samples
            pTcd[c-1][d] = np.sum(feature_column == 'T') / total_samples


    # your implementation ends above
    return(pAcd, pCcd, pGcd, pTcd)

pAcd, pCcd, pGcd, pTcd = estimate_nucleotide_probabilities(X_train, y_train)
print(pAcd)
print(pCcd)
print(pGcd)
print(pTcd)



# STEP 6
# assuming that there are N data points and K classes
# should return a numpy array with shape (N, K)
def calculate_score_values(X, pAcd, pCcd, pGcd, pTcd, class_priors):
    # your implementation starts below
    K = max(y)  # Number of classes (assuming y starts from 0)
    N, D = X.shape  # Number of data entries, number of features

    # Init score with priors
    score_values = [np.log(x) for x in class_priors]
    score_values = np.tile(np.log(class_priors), (N, 1))

    #
    pXcd = {"A":pAcd, "C":pCcd, "G":pGcd, "T":pTcd}

    # # Add feature Likelihoods
    # for i, row in X:
    #     for d in row:
    #         np.log(pXcd[d][i])

    # Loop through each data point
    for i in range(N):
        # Loop through each class
        for j in range(K):
            # Loop through each feature (nucleotide in the sequence)
            for d in range(D):
                nucleotide = X[i][d]
                score_values[i, j] += np.log(pXcd[nucleotide][j, d])

    # your implementation ends above
    return(score_values)

scores_train = calculate_score_values(X_train, pAcd, pCcd, pGcd, pTcd, class_priors)
print(scores_train)

scores_test = calculate_score_values(X_test, pAcd, pCcd, pGcd, pTcd, class_priors)
print(scores_test)



# STEP 7
# assuming that there are K classes
# should return a numpy array with shape (K, K)
def calculate_confusion_matrix(y_truth, scores):
    # your implementation starts below
    K = scores.shape[1]  # Number of classes
    N = len(y_truth)  # Number of data points
    
    # Initialize confusion matrix with zeros
    confusion_matrix = np.zeros((K, K))
    
    # Find the predicted class labels
    predicted_classes = np.argmax(scores, axis=1)
    
    # Populate the confusion matrix
    for n in range(N):
        true_class = y_truth[n]
        predicted_class = predicted_classes[n]
        confusion_matrix[true_class-1][predicted_class] += 1  
    # your implementation ends above
    return(confusion_matrix)

confusion_train = calculate_confusion_matrix(y_train, scores_train)
print(confusion_train)

confusion_test = calculate_confusion_matrix(y_test, scores_test)
print(confusion_test)
