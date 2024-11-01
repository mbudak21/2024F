import matplotlib.pyplot as plt
import numpy as np

true_labels = np.genfromtxt("hw06_true_labels.csv", delimiter = ",", dtype = "int")
predicted_probabilities = np.genfromtxt("hw06_predicted_probabilities.csv", delimiter = ",")

# STEP 3
# given the predicted probabilities of size (N,),
# it should return the calculated thresholds of size (N + 1,)
def calculate_threholds(predicted_probabilities):
    # your implementation starts below
    sorted_probs = np.sort(predicted_probabilities)

    thresholds = [(a + b) / 2 for a, b in zip(sorted_probs, sorted_probs[1:])]

    thresholds.insert(0, sorted_probs[0] / 2)
    thresholds.append((sorted_probs[-1] + 1) / 2)

    thresholds = np.array(thresholds)

    # your implementation ends above
    return thresholds

thresholds = calculate_threholds(predicted_probabilities)
#print(thresholds)

# STEP 4
# given the true labels of size (N,), the predicted probabilities of size (N,) and
# the thresholds of size (N + 1,), it should return the FP and TP rates of size (N + 1,)
def calculate_fp_and_tp_rates(true_labels, predicted_probabilities, thresholds):
    # your implementation starts below

    TPs = np.zeros(len(thresholds))
    FPs = np.zeros(len(thresholds))
    
    for i in range(len(thresholds)):
        negative_true = 0
        negative_false = 0
        positive_true = 0
        positive_false = 0

        current_threshold = thresholds[i]

        for j in range(len(true_labels)):
            if predicted_probabilities[j] >= current_threshold:
                if true_labels[j] != 1:
                    positive_false += 1
                else:
                    positive_true += 1
            if predicted_probabilities[j] < current_threshold:
                if true_labels[j] != 1:
                    negative_true += 1
                else:
                    negative_false += 1

        FPs[i] = (positive_false / (positive_false + negative_true))
        TPs[i] = (positive_true / (positive_true + negative_false))

    # your implementation ends above
    return FPs, TPs

fp_rates, tp_rates = calculate_fp_and_tp_rates(true_labels, predicted_probabilities, thresholds)
print(fp_rates)
print(tp_rates)

fig = plt.figure(figsize = (5, 5))
plt.plot(fp_rates, tp_rates)
plt.xlabel("FP Rate")
plt.ylabel("TP Rate")
plt.show()
fig.savefig("hw06_roc_curve.pdf", bbox_inches = "tight")

# STEP 5
# given the FP and TP rates of size (N + 1,),
# it should return the area under the ROC curve
def calculate_auroc(fp_rates, tp_rates):
    # your implementation starts below
    sorted_indices = np.argsort(fp_rates)
    sorted_fp_rates = fp_rates[sorted_indices]
    sorted_tp_rates = tp_rates[sorted_indices]

    auroc = 0.0
    for i in range(1, len(sorted_fp_rates)):
        # Calculate the width and the average height of the trapezoid
        width = sorted_fp_rates[i] - sorted_fp_rates[i - 1]
        height = (sorted_tp_rates[i] + sorted_tp_rates[i - 1]) / 2
        # Add the area of the trapezoid to the total area
        auroc += width * height
    # your implementation ends above
    return  auroc

auroc = calculate_auroc(fp_rates, tp_rates)
print("The area under the ROC curve is {}.".format(auroc))