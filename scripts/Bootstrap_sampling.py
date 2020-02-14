# File created by Miyuraj Harishchandra Hikkaduwa Withanage
import pandas as pd
from sklearn.preprocessing import label_binarize
from matplotlib import pyplot as plt
from sklearn.naive_bayes import GaussianNB
import os

from itertools import combinations
from venn import venn
import numpy as np
import sys
import glob
from shutil import copyfile


print(os.getcwd())
# current directory of second file
curr_dir=os.getcwd()
current_Sec = os.getcwd()+"/input.csv"
# First argument takes a CSV file as an input
#filepath=sys.argv[1]



#filepath="./pipe_step_1_Bootsrapping/input_file/input.csv"
dataset_DP2 = pd.read_csv(current_Sec)
Y = dataset_DP2.iloc[:,dataset_DP2.shape[1]-1:dataset_DP2.shape[1]]


X= dataset_DP2.iloc[:,0:dataset_DP2.shape[1]-1]
print("")
print("You are about to perform bootstrap sampling of the input file.")
print("")
print("------------------------Input File----------------")
print("1. No of features = "+str(dataset_DP2.shape[1]))
print("2. No of observations = "+str(dataset_DP2.shape[0]))
print("--------------------------------------------------")
print("")
print("To perform bootstrap sampling, user need to specify following thresholds.")
print("------------------------Thresholds----------------")
print("1. Sampling Fraction: Fraction of the features to be used.")
print("2. No. of samples to be make for bootstrapping.")
print("--------------------------------------------------")

# following input (which comes as string) is converted to float as it
SampFrac = float(input("What's the sampling fraction? (Answer should be between 0 and 1) : "))
print("")
print("Sampling fraction is set to "+ str(SampFrac))
print("--------------------------------------------------")
print("")
Number_of_samples = int(input("What's the No. of samples to be drawn for bootstrapping? : "))
#print("No. of samples to be drawn is set to "+ str(Number_of_samples))
print("--------------------------------------------------")
print("")
print("")


# Binarize the output
print("-----------------class labels of the input files------------------------")
print("Before proceeding, we have to binarize the class labels.")
print("")
# extracting out the last column of teh dataset
last_col = dataset_DP2.iloc[:, -1]
# using the set function to get the unique values
set_last_col = set(last_col)
print("The class labels of the file are ", end='')
print(set_last_col)
class_labels_in_all = list(set_last_col)
print("")
print("Please, assign the positive label. Then, the negative label is inferred.")
#Join =input("type yes")
print("Is " + class_labels_in_all[0]+" your positivle class label?")
Join =input("Type Y for yes and N for no :\n")
# Numeric_class_labels is the list where I store the nummeric labels
numeric_class_labels=[]
if Join == 'yes' or Join == 'Yes'or Join == 'Y'or Join == 'y' or Join == 'YES':
    print("You typed yes.")
    print(class_labels_in_all[0]+" will be modified as 1")
    for item in range(1, Y.shape[0]+1):
        #print(Y.shape)
        # to convert the pandas data frame to list use the folloing method
        dataframe_into_list=Y.iloc[item-1:item].values.tolist()
        flat=[item for items in dataframe_into_list for item in items]
        #print(flat[0])
        #print(class_labels_in_all[0])
        if flat[0] == str(class_labels_in_all[0]):
            numeric_class_labels.append(1)
        else:
            numeric_class_labels.append(0)

else :
    print("You did not type yes. Because of that, ",end='')
    print(class_labels_in_all[1] + " will be modified as 0")
    for item in range(1, Y.shape[0]+1):
        # print(Y.shape)
        # to convert the pandas data frame to list use the folloing method
        dataframe_into_list = Y.iloc[item - 1:item].values.tolist()
        flat = [item for items in dataframe_into_list for item in items]
        # print(flat[0])
        # print(class_labels_in_all[0])
        if flat[0] == str(class_labels_in_all[0]):
            numeric_class_labels.append(0)
        else:
            numeric_class_labels.append(1)

label_pd = pd.DataFrame()
label_pd['class'] = numeric_class_labels
# np.asarray needed for sklearn class label input
label_pd = np.asarray(label_pd)
#print(Y)
#print(Y.shape)
#print("===")
#print(label_pd.shape)
##print(label_pd)
#print("===")
#print("===")
#exit()
#print(label_pd)



#

#Y = label_binarize(Y, classes=['Iris-setosa', 'Iris-versicolor'])
#print(Y)
#exit()
#n_classes = Y.shape[1]


# sampling fraction
#SampFrac = 0.60
# Number of samples

# This will store AUC values
AUC_list = []
NB_list = []

# THis will store the feature set of each bootstrap sample
# Bootstrap sample's will be named as 1,2,3,..n etc.
sample_dictionary = dict()
venn_dictionary = dict()
AUC_dictionary = dict()
#Number_of_samples = 100
number_of_attri=0
for key in range(1,Number_of_samples):
    bootsrap_sample = ((X.T).sample(frac=0.6, replace=True)).T
    Xx = bootsrap_sample.to_numpy()

    # extract feature names from split
    colname_list=list(bootsrap_sample.columns[0:bootsrap_sample.shape[1]])
    bootsrap_sample['class'] = label_pd
    # create a dictionary using colname
    sample_dictionary[key] = colname_list
    venn_dictionary[key] = set(colname_list)
    #print(set(colname_list))
    #print(venn_dictionary)
    number_of_attri=bootsrap_sample.shape[1]

    from sklearn.model_selection import StratifiedKFold


    nsplitting = 3
    skf = StratifiedKFold(n_splits=nsplitting)
    random_state = 12883823
    count = 0
    # nsplitting = 5
    # rf = KFold(n_splits=nsplitting, random_state=random_state)
    # y_score is gonna be used outside loop
    # y_score=dict()
    # concat_y_score = float()
    # concat_y_test = float()
    button = False
    A = []
    total = 0
    test_temp = []
    auc_all = 0
    # label_pd is the pandas dataframe containing numeric class labels

    for train_index, test_index in skf.split(Xx, label_pd):
        # print("TRAIN:", train_index, "TEST:", test_index)
        train_features, test_features = Xx[train_index], Xx[test_index]
        train_labels, test_labels = label_pd[train_index], label_pd[test_index]
        # from sklearn.svm import SVC
        # rf = SVC(gamma='auto', probability=True)
        from sklearn.naive_bayes import ComplementNB

        rf = GaussianNB()
        # print("labels")
        # print(train_labels)
        #print("train features"+str(train_features.shape))
        #print("train labels" + str(train_labels.shape))
        rf.fit(train_features, train_labels.ravel())
        from sklearn.metrics import roc_curve, auc

        y_pred_rf = rf.predict_proba(test_features)[:, 1]
        #print(test_features[:,test_features[1]-1:test_features[1]])
        #print(rf.predict_proba(test_features)[:, 1])
        #print(test_labels)
        # print(test_labels)
        # print("******")

        # print(y_pred_rf)
        total = y_pred_rf.shape[0] + total
        count = count + 1
        # array
        fpr_rf, tpr_rf, _ = roc_curve(test_labels, y_pred_rf)
        roc_auc = auc(fpr_rf, tpr_rf)
        # cannot concatenate without tolist()
        auc_all = auc_all + roc_auc

    # print("==========================================")
    # print(auc_all)
    average_auc = auc_all / count
    #print("test")

    AUC_dictionary[key] = average_auc
    #print(AUC_dictionary[key])

# ascending order of the AUC dictionary
##
# converting the dictionary into a list
list_dictionary = list(AUC_dictionary.items())

#In Python Dictionary, items() method is used to return the list
#with all dictionary keys with values.

def Sort(sub_li):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    return (sorted(sub_li, key=lambda x: x[1],reverse=True))

sorted_list_dictionary = Sort(list_dictionary)
#print(sorted_list_dictionary)

#dict=dict(sorted_list_dictionary) # convert the list in dictionary
#print(dict)

#print("Number of Features in a bootstrap sample is ",end='')
#print(number_of_attri)

#print("Pick the bootstrap samples generating greater than 0.90")
# cut_off key is the key value for feature lists greater than .90 AUC
cutt_off_key = 0
counter_to_index_threshold = 0
for iterat in range(0,len(sorted_list_dictionary)):
    if sorted_list_dictionary[iterat][1] > .90:
        counter_to_index_threshold=iterat
        #print("Updating threshold... "+str(sorted_list_dictionary[l][0]))
        cutt_off_key=sorted_list_dictionary[iterat][0]
    else:
        break
# list of sets is used to append all the promising bootstrap splits into the it
sets=[]

# sorted_list_dictionary is a list withAUC and split numbers
for l in range(0,counter_to_index_threshold):
    #print(sorted_list_dictionary[l])
    #get AUC value
    #print(sorted_list_dictionary[l][1])
    #get split number
    key=sorted_list_dictionary[l][0]
    # use it as a key to the very first dictionary (sample_dictionary) to get the feature list
    #print(sample_dictionary[key])
    sets.append(set(sample_dictionary[key]))

#print(sets)
os.chdir('../../pipe_step_3_FAggregation/pipe_step_3_make_venn/output_vennDiagram/')


f_arrangement_file = open("feature_set_arrangement.txt", "a")
for comboSize in range(1,len(sets)+1):
    ##print("combosize is "+str(comboSize))
    tempset = list()
    unitedtempset = list()
    for combo in combinations(range(len(sets)),comboSize):
        intersection = sets[combo[0]]
        for i in combo[1:]: intersection = intersection & sets[i]
        statement =" and ".join(f"Set{i+1}" for i in combo),"=",intersection
        #print(statement)
        #f_arrangement_file.write(statement)
        f_arrangement_file.write(' '.join(str(s) for s in statement) + '\n')
        ##print("====")
        unitedtempset.append(list(intersection))
    #print("combosize is " + str(comboSize))
    ##print(unitedtempset)
    # make a flat list from list of lists
    flat_list = [item for sublist in unitedtempset for item in sublist]
    ##print(flat_list)
    ##print("get only uniques of flat list")
    flat_list_with_uniques=list(set(flat_list))
    #print("following is flat_list_with_uniques")
    flat_list_with_uniques.append("class")
    #print(flat_list_with_uniques)
    transposed = dataset_DP2.T
    reversed = transposed.loc[flat_list_with_uniques].T
    #print(reversed)


    #need to transpose the list to be saved in csv file
    #df_list=pd.DataFrame(flat_list_with_uniques)
    ##print(df_list)
    os.chdir(curr_dir)
    os.chdir("../output_feature_aggregates/")
    reversed.to_csv("at_Least.%s.csv" % comboSize, sep=',',index=False,header=True)
    #reversed.to_csv("./../pipe_step_1_Bootsrapping/output_feature_aggregates/at_Least.%s.csv" % comboSize, sep=',',index=False, header=True)

    #reversed.to_csv("/Users/miyuraj/Documents/M2ROC/M2ROC_CommandLine/pipe_step_3_FAggregation/pipe_step_3_make_aggregates/at_Least.%s.csv" % comboSize,sep=',', index=False, header=True)


print("")
print("Bootstrap processing complete.")
print("Bootstrap aggregate files are located in ./pipe_step_1_Bootstrapping/output_feature_aggregates/")
print("")
print("---------------")
print("Total features in the input file: "+str(dataset_DP2.shape[1]))
print("")
print("Feature Aggregate Name  -->  No.of Features --> Percentage")

# adding csv files with path to a list
# long names for copying to feature selection folder
csv_option_list_help_list=[]
# short names for menu display
csv_option_list_help_list_shortnames=[]
# Iterate through all the csv files
#print(os.getcwd())
#exit()
os.chdir('.')
csvFiles = sorted(glob.glob('*.csv'))
for filepicker in range(0, len(csvFiles)):
    #color_count = color_count + 1
    FeatureAggrecsv = pd.read_csv(os.getcwd() + '/' + csvFiles[filepicker], delimiter=',')
    csv_option_list_help_list.append(os.getcwd() + '/' + csvFiles[filepicker])
    csv_option_list_help_list_shortnames.append(csvFiles[filepicker])
    print(str(filepicker+1)+". "+csvFiles[filepicker]+" --> " + str(FeatureAggrecsv.shape[1]-1)+" --> " +str(round(((FeatureAggrecsv.shape[1]-1)*100)/(dataset_DP2.shape[1]),2))+"%")

#os.chdir('../../')
#os.chdir('./pipe_step_2_FS/pipe_step_2_input/')
os.chdir('.')
print("")
print("-------------------------")
print("Please, choose a file from above table to be sent to feature selection: ")
chosen_file=int(input("Enter the file number of the selected file: "))
print("")
print("You picked file: "+csv_option_list_help_list_shortnames[chosen_file-1])
print("")
print("-------------------------")

#copyfile(csv_option_list_help_list[chosen_file-1], '../../pipe_step_2_FS/pipe_step_2_input/input.csv')
copyfile(csv_option_list_help_list[chosen_file-1], '../../pipe_step_2_FS/pipe_step_2_input/input.csv')

print("")
print(csv_option_list_help_list[chosen_file-1] + " was copied to ./pipe_step_2_FS/pipe_step_2_input/ as input.csv")
print("")
print("Please, run the following bash script for feature selection.")
print("             bash ./run_step_2_FeatureSelection.sh")
# returning to original working folder



f_arrangement_file.close()
#plt.show()



