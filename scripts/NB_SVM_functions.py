######################################
#   Miyuraj Harishchandra Hikkaduwa Withanage
#
#   This will calculate AUC for aggregates and create a pandas dataframe
#
######################################

import os
import numpy as np
import glob  # python pattern matching
import pandas as pd
import matplotlib

matplotlib.use("TkAgg")
from matplotlib import pyplot as plt




def functionNB(path):
    # os.chdir(
    #    '/Users/miyuraj/Documents/M2ROC/ZhangProject/class1/pipe_step_3_FAggregation/pipe_step_3_make_aggregates/at_Least.1')
    os.chdir(path)
    print("Naive Bayes Classifier Started.")

    csvFiles = sorted(glob.glob('*.csv'))

    print(csvFiles)

    plt.figure(1)

    colors = ['red', 'navy', 'orange', 'dodgerblue', 'magenta', 'brown', 'purple', 'green', 'gold', 'lawngreen', 'aqua',
              'gray']
    # os.remove("ComplementNB_AUC.txt")
    # f = open("ComplementNB_AUC.txt", "w")
    # color_count = 0
    NB_ROC_AUC_list = []
    for filepicker in range(0, len(csvFiles)):
        # color_count = color_count + 1
        print(csvFiles[filepicker])
        dataCSV = pd.read_csv(os.getcwd() + '/' + csvFiles[filepicker], delimiter=',', header=0)
        dataCSV_dummy = pd.get_dummies(dataCSV)
        dataCSV_dummy = dataCSV_dummy.to_numpy()
        labels = dataCSV_dummy[:, dataCSV_dummy.shape[1] - 1:dataCSV_dummy.shape[1]]
        # print(labels)
        # labels = labels.ravel()
        features = dataCSV_dummy[:, 0: dataCSV_dummy.shape[1] - 1]

        X = allData = dataCSV_dummy[:, 0:dataCSV_dummy.shape[1] - 1]
        if X.shape[1] < 1:
            # print(np.array(0))
            NB_ROC_AUC_list.append(np.array(0))
            continue

        from sklearn.model_selection import LeaveOneOut

        loo = LeaveOneOut()
        loo.get_n_splits(X)

        random_state = 12883823

        testlabel_list = []
        predictionoutput_list = []
        for train_index, test_index in loo.split(X, labels):
            train_features, test_features = X[train_index], X[test_index]

            train_labels, test_labels = labels[train_index], labels[test_index]

            from sklearn.naive_bayes import ComplementNB

            rf = ComplementNB()

            rf.fit(train_features, train_labels.ravel())
            from sklearn.metrics import roc_curve, auc
            y_pred_rf = rf.predict_proba(test_features)[:, 1]

            test_labels_flat = [item for sublist in test_labels for item in sublist]

            testlabel_list.append(test_labels_flat)
            predictionoutput_list.append(y_pred_rf)

        fpr_rf, tpr_rf, _ = roc_curve(np.asarray(testlabel_list), predictionoutput_list)
        roc_auc = auc(fpr_rf, tpr_rf)

        NB_ROC_AUC_list.append(roc_auc)

    return list(np.array(NB_ROC_AUC_list))


# this should take a file and return auc value
# this script is woriking fine.
# it is used to create the SVM curve for a given ranked feature set




def functionSVM(path):
    #os.chdir(
    #    '/Users/miyuraj/Documents/M2ROC/ZhangProject/class1/pipe_step_3_FAggregation/pipe_step_3_make_aggregates/at_Least.1')
    os.chdir(path)
    print("SVM Classifier Started.")

    csvFiles = sorted(glob.glob('*.csv'))
    #csvFiles = (glob.glob('*.csv')

    print(csvFiles)

    plt.figure(1)

    colors = ['red', 'navy', 'orange', 'dodgerblue', 'magenta', 'brown', 'purple', 'green', 'gold', 'lawngreen', 'aqua',
              'gray']


    # color_count = 0
    SVC_ROC_AUC_list = []
    for filepicker in range(0, len(csvFiles)):
        # color_count = color_count + 1
        #print(csvFiles[filepicker])
        dataCSV = pd.read_csv(os.getcwd() + '/' + csvFiles[filepicker], delimiter=',', header=0)
        dataCSV_dummy = pd.get_dummies(dataCSV)
        dataCSV_dummy = dataCSV_dummy.to_numpy()
        labels = dataCSV_dummy[:, dataCSV_dummy.shape[1] - 1:dataCSV_dummy.shape[1]]
        # print(labels)
        # labels = labels.ravel()
        features = dataCSV_dummy[:, 0: dataCSV_dummy.shape[1] - 1]


        X = allData = dataCSV_dummy[:, 0:dataCSV_dummy.shape[1] - 1]
        if X.shape[1] < 1:
            #print(np.array(0))
            SVC_ROC_AUC_list.append(np.array(0))
            continue

        from sklearn.model_selection import LeaveOneOut

        loo = LeaveOneOut()
        loo.get_n_splits(X)

        random_state = 12883823

        testlabel_list = []
        predictionoutput_list = []
        for train_index, test_index in loo.split(X, labels):
            train_features, test_features = X[train_index], X[test_index]

            train_labels, test_labels = labels[train_index], labels[test_index]
            from sklearn.svm import SVC
            rf = SVC(gamma='auto', probability=True)

            rf.fit(train_features, train_labels.ravel())
            from sklearn.metrics import roc_curve, auc
            y_pred_rf = rf.predict_proba(test_features)[:, 1]

            test_labels_flat = [item for sublist in test_labels for item in sublist]

            testlabel_list.append(test_labels_flat)
            predictionoutput_list.append(y_pred_rf)


        fpr_rf, tpr_rf, _ = roc_curve(np.asarray(testlabel_list), predictionoutput_list)
        roc_auc = auc(fpr_rf, tpr_rf)


        SVC_ROC_AUC_list.append(roc_auc)

    return list(np.array(SVC_ROC_AUC_list))

