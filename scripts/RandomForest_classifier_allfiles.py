################################################
#   Part of BEAR Pipeline
#   Created by: Miyuraj Harishchandra Hikkaduwa Withanage
#   University of Iowa
#   Random Forest Classifier Script
#   bootstrap=True, n_estimators=30, random_state=45, max_features="auto",
#                                         max_depth=1000, criterion="gini"
##############################################

print("RF Classification Started.")
import numpy as np

from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from sklearn import metrics
from scipy import interp
import csv
import os, sys  # need to import current working directory
import glob # python pattern matching
import re # regular expression
from numpy import genfromtxt #to open csv file
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

# Get the list of csv files in the working directory
csvFiles = sorted(glob.glob('*.csv'))
# Initiating a plot
plt.figure(1)
# Specifying colors used in the plot
colors = ['red','navy','orange','dodgerblue','magenta','brown','purple','green','gold','lawngreen','aqua','gray']
# SVM_AUC Data Frame to Store AUC values
SVM_AUC = pd.DataFrame()

# Read each file in csvFiles list
for filepicker in range(0, len(csvFiles)):
    # Read the fie into dataCSV dataframe (Pandas)
    dataCSV = pd.read_csv(os.getcwd() + '/' + csvFiles[filepicker], delimiter=',',header=0)
    dataCSV_dummy = pd.get_dummies(dataCSV)
    # Convert values of dataframe to numeric values
    dataCSV_dummy = dataCSV_dummy.to_numpy()
    # Identify labels in dataframe
    labels = dataCSV_dummy[:, dataCSV_dummy.shape[1] - 1:dataCSV_dummy.shape[1]]
    # Get the feature set separated
    features = dataCSV_dummy[:, 0: dataCSV_dummy.shape[1]-1]
    SVM_list = []

    # creating different feature sets by incrementing the size of feature set
    for iterator in range(1, dataCSV_dummy.shape[1]):
        # feature set
        X = allData = dataCSV_dummy[:, 0:iterator]
        # Use leave one out cross validation
        from sklearn.model_selection import LeaveOneOut
        loo = LeaveOneOut()
        loo.get_n_splits(X)

        random_state = 12883823

        test_temp = []
        testlabel_list = []
        predictionoutput_list = []

        # LOO-CV Procedure (train, test splitting)
        for train_index, test_index in loo.split(X,labels):
            # creating train set and test set (features)
            train_features, test_features = X[train_index], X[test_index]
            # creating train set and test set (class labels)
            train_labels, test_labels = labels[train_index], labels[test_index]

            # importaing  RF Classifier libraries
            from sklearn.ensemble import RandomForestClassifier
            # Defining RF classifier
            rf = RandomForestClassifier(bootstrap=True, n_estimators=30, random_state=45, max_features="auto",
                                        max_depth=1000, criterion="gini")
            # Model fitting (Training)
            rf.fit(train_features, train_labels.ravel())

            # Ready to calculate ROC curve and AUC
            from sklearn.metrics import roc_curve, auc
            # Make predictions based on fitted model
            y_pred_rf = rf.predict_proba(test_features)[:, 1]
            test_labels_flat = [item for sublist in test_labels for item in sublist]

            # we make a list of test labels and prediction output over the crossvalidation
            # we use this entire set to calculate the ROC and AUC
            # Test_labels and y_pred_rf are numpy nd.array
            testlabel_list.append(test_labels_flat)
            predictionoutput_list.append(y_pred_rf)

        # Calculate TPR and FPR using testlabel_list and predictionoutput_list
        fpr_rf, tpr_rf, _ = roc_curve(np.asarray(testlabel_list), predictionoutput_list)
        roc_auc = auc(fpr_rf, tpr_rf)
        SVM_list.append(roc_auc)
    # At this point we have AUC values for each csv file
    # This is a Pandas dataframe
    SVM_AUC[csvFiles[filepicker].replace('.csv', '')] = SVM_list
    SVM_list = np.asarray(SVM_list)
    # Creating X Axis
    xaxis = list(range(1, dataCSV_dummy.shape[1]))
    xaxis = np.asarray(xaxis)
    lw = 2
    # plt.plot(fpr_rf, tpr_rf, label='ROC curve of class {0} (area = {1:0.2f})' ''.format(i, roc_auc[i]))
    plt.plot(np.asarray(xaxis), np.asarray(SVM_list), color=colors[filepicker], lw=lw, label='{0}' ''.format(re.sub('.csv', '', str(csvFiles[filepicker]))))
    plt.xlim(0, len(xaxis))
    plt.ylim(0, 1.1)
    plt.ylabel('Area Under ROC curve')
    plt.xlabel('Ranked Features')
    plt.title('AUC (RF Classifier) VS. Ranked Feature Curve')
    plt.legend(loc="lower right")
    plt.savefig("../../result_classifier_evalutions/RF_AUV_vs_RankedFeature_Curve.pdf")
SVM_AUC.to_csv('../../result_auc_for_each_position/RF_AUC.csv',sep=',',index=False,header=True)
#plt.show()
print("RF Classification Complete.")




