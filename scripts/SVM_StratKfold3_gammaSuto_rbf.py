# File created by Miyuraj Harishchandra Hikkaduwa Withanage

print("SVM Classification Started.")
import numpy as np
#import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
#from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
#from sklearn.cross_validation import KFold
#from sklearn.cross_validation import LeaveOneOut
#from sklearn import cross_validation
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

#from sys import platform as sys_pf
#if sys_pf == 'darwin':
    #import matplotlib
    #matplotlib.use("TkAgg")
csvFiles = sorted(glob.glob('*.csv'))
#print(csvFiles)
plt.figure(1)
#plt.plot([0, 1], [0, 1], 'k--')
colors = ['red','navy','orange','dodgerblue','magenta','brown','purple','green','gold','lawngreen','aqua','gray']
#os.remove("SVM_AUC.txt")
f = open("../../result_auc_for_each_position/SVM_AUC.txt", "a")
#color_count = 0
for filepicker in range(0, len(csvFiles)):
    #color_count = color_count + 1
    dataCSV = pd.read_csv(os.getcwd() + '/' + csvFiles[filepicker], delimiter=',',header=0)
    dataCSV_dummy = pd.get_dummies(dataCSV)
    dataCSV_dummy = dataCSV_dummy.to_numpy()
    labels = dataCSV_dummy[:, dataCSV_dummy.shape[1] - 1:dataCSV_dummy.shape[1]]
    labels = labels.ravel()
    features = dataCSV_dummy[:, 0: dataCSV_dummy.shape[1]-1]
    SVM_list = []
    for iterator in range(1, dataCSV_dummy.shape[1]):
        # target class column
        # y = targets = my_data[:, my_data.shape[1] - 1:my_data.shape[1]]
        # full dataset
        # if topSet == 0:
        #    topSet = dataCSV_dummy.shape[1]
        X = allData = dataCSV_dummy[:, 0:iterator]
        # binarize for four classes
        labels = label_binarize(labels, classes=[0,1])
        n_classes = labels.shape[1]

        from sklearn.model_selection import train_test_split
        from sklearn.model_selection import KFold
        from sklearn.model_selection import StratifiedKFold

        # if binary class, stratified Kfold needs to be used
        nsplitting = 5
        skf = StratifiedKFold(n_splits=nsplitting)
        random_state = 12883823
        count = 0
        #nsplitting = 5
        #rf = KFold(n_splits=nsplitting, random_state=random_state)
        # y_score is gonna be used outside loop
        # y_score=dict()
        # concat_y_score = float()
        # concat_y_test = float()
        button = False
        A = []
        total =0
        test_temp = []
        auc_all = 0
        for train_index, test_index in skf.split(X,labels):
            ##print("TRAIN:", train_index, "TEST:", test_index)
            train_features, test_features = X[train_index], X[test_index]
            train_labels, test_labels = labels[train_index], labels[test_index]
            from sklearn.svm import SVC
            rf = SVC(kernel='linear', probability=True)
            ##print("labels")
            ##print(train_labels)
            rf.fit(train_features, train_labels.ravel())
            from sklearn.metrics import roc_curve, auc
            y_pred_rf = rf.predict_proba(test_features)[:, 1]
            ##print("***********")
            ##print(test_labels)
            ##print("******")

            ##print(y_pred_rf)
            total = y_pred_rf.shape[0]+total
            count = count +1
            # array
            fpr_rf, tpr_rf, _ = roc_curve(test_labels, y_pred_rf)
            roc_auc = auc(fpr_rf, tpr_rf)
            # cannot concatenate without tolist()
            auc_all = auc_all+roc_auc




        #print("==========================================")
        #print(auc_all)
        average_auc = auc_all/count
        ##print(np.asarray(A))
        ##print(np.asarray(test_temp))
        ##print(np.asarray(y_pred_rf).ravel())
        ##print(np.asarray(test_labels_vector).ravel())
        #print("=====")
        ##print(fpr_rf_list)
        ##print(tpr_rf_list)

        SVM_list.append(average_auc)
        #print("round complete ===============" + str(count)+ "==> AUC: " + str(average_auc))
        iterator = iterator + 1
    ##print("=================================")
    ##print(csvFiles[filepicker])
    f.write(csvFiles[filepicker]+"\n")
    ##print("#printing SVM list")
    f.write(str(SVM_list)+"\n")
    # #print(SVM_list)
    ##print(len(SVM_list))
    SVM_list = np.asarray(SVM_list)
    ##print(SVM_list)

    ##print("#printing X axis")
    xaxis = list(range(1, dataCSV_dummy.shape[1]))

    ##print(len(xaxis))
    xaxis = np.asarray(xaxis)
    ##print(xaxis)
    #plt.figure()
    # plt.plot([0, 1], [0, 1], 'k--')

    lw = 2
    # plt.plot(fpr_rf, tpr_rf, label='ROC curve of class {0} (area = {1:0.2f})' ''.format(i, roc_auc[i]))
    plt.plot(np.asarray(xaxis), np.asarray(SVM_list), color=colors[filepicker], lw=lw, label='{0}' ''.format(re.sub('.csv', '', str(csvFiles[filepicker]))))
    plt.xlim(0, len(xaxis))
    plt.ylim(0, 1.1)
    plt.ylabel('Area Under ROC curve')
    plt.xlabel('Ranked Features')
    plt.title('AUC (SVM Classifier) VS. Ranked Feature Curve')
    plt.legend(loc="lower right")
    plt.savefig("../../result_classifier_evalutions/SVM_AUV_vs_RankedFeature_Curve.pdf")
#plt.show()
print("SVM Classification Complete.")




