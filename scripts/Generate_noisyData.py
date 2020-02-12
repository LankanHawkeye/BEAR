import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle

from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from scipy import interp
from sklearn.metrics import roc_auc_score
import pandas as pd

# Import some data to play with
#iris = datasets.load_iris()
#X = iris.data
#y = iris.target
#print()
# opening the data file as pandas data frame
dataset_DP2 = pd.read_csv("/Users/miyuraj/Documents/M2ROC/iris.temp.csv")
# extracting the relevent columns for x and y
X = dataset_DP2.iloc[:,0:dataset_DP2.shape[1]-1]
# converting pd df to numpy array
X= np.asarray(X)
# extrating Y data
Y = dataset_DP2.iloc[:,dataset_DP2.shape[1]-1:dataset_DP2.shape[1]]


# Binarize the output
#y = label_binarize(y, classes=[0, 1, 2])
#n_classes = y.shape[1]

# Add noisy features to make the problem harder
random_state = np.random.RandomState(0)
n_samples, n_features = X.shape
X = np.c_[X, random_state.randn(n_samples, 200 * n_features)]
# NB classifier cannot take negative values
# turn all negatives to positive hence absolute values
Xabs = np.absolute(X)
# Round the whole numpy matrix to two decimal places
Xabs=np.matrix.round(Xabs,  decimals=2)

#convert the numpy matrix to pandas dataframe back
X=pd.DataFrame(Xabs)
# Addiing the labels back
X['class'] = Y

# Saving the data in input folder
X.to_csv('/Users/miyuraj/Documents/M2ROC/M2ROC_CommandLine/input_file/new.csv',sep=',',header=True)
