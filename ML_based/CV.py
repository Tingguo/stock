# Moving window cross-validation

import numpy as np
from machineLearning import Classify
def CV(X_train, y_train, number_folds, algorithm):
    """
	Given X_train and y_train (the test set is excluded from the Cross Validation),
    number of folds, the ML algorithm to implement and the parameters to test,
    Returns mean of test accuracies.
    """

    k = int(np.floor(float(X_train.shape[0]) / number_folds))
    accuracies = np.zeros(number_folds-1)

    # loop from the first 2 folds to the total number of folds
    for i in range(2, number_folds + 1):
        print('')
        X = X_train[:(k*i)]
        y = y_train[:(k*i)]
        split = float(i-1)/i
        index = int(np.floor(X_train.shape[0] * split))
        # folds used to train the model
        X_trainFolds = X_train[:index]
        y_trainFolds = y_train[:index]
        # fold used to test the model
        X_testFold = X_train[(index + 1):]
        y_testFold = y_train[(index + 1):]
        accuracies[i-2] = Classify(X_trainFolds, y_trainFolds, X_testFold, y_testFold, algorithm)
        print('Accuracy on fold ' + str(i) + ': ', accuracies[i-2])
    return accuracies.mean()
