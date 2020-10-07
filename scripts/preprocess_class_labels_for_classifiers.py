# File created by Miyuraj Harishchandra Hikkaduwa Withanage
import os,glob
import pandas as pd
import re


def feature_preprocess(path):
    # access the folder
    os.chdir(path)
    # get all csv files names into a list called csvFiles
    csvFiles = glob.glob('*.csv')
    # print(csvFiles)
    # following empty list is for storing total class labels in the file set
    total_class_labels = []
    for filepicker in range(0, len(csvFiles)):
        current_file_path = csvFiles[filepicker]
        # print(current_file_path)
        # read current file into a dataframe
        current_file = pd.read_csv(current_file_path, sep=',')
        # print(current_file)

        # print(current_file.columns.tolist()[-1])
        # print("Last column of this file ("+current_file_path+") is "+ current_file.columns.tolist()[-1]+".")
        # print("It contains following unique labels.")
        # print("================================")
        # selecting gthe last columns
        last_col = current_file.iloc[:, -1]
        # print(list(set(last_col)))
        # print("")
        # print("")
        # adding total class labels found.
        total_class_labels.append(list(set(last_col)))

    # print("Here are the different class labels found in this entire collection of files. Please, review them carefully.")
    # print("Hint: Spelling mistakes can create more class labels")
    # make a flat list from list of lists
    print("")

    PATHNAME_1=path.replace('./../','')
    PATHNAME_1 = PATHNAME_1.replace('/', '')
    print("Creating numeric class labels for files in "+PATHNAME_1+" folder")
    flat_list = [item for sublist in total_class_labels for item in sublist]
    class_labels_in_all = sorted(list(set(flat_list)))
    print(class_labels_in_all[0] + " will be modified as 1")
    print(class_labels_in_all[1] + " will be modified as 0")
    os.system("for f in *csv;do sed -i -e 's#'{0}'#1#g' $f;done".format(class_labels_in_all[0]))
    os.system("for f in *csv;do sed -i -e 's#'{0}'#0#g' $f;done".format(class_labels_in_all[1]))
    os.system("rm *e")
    print("")
    print("==========================")
    # print(list(set(flat_list)))

    # print("Proceeding with the program will allow you to pick the positive label. Negative label is inferred.")
    # Join =input("type yes")
    # print("Is " + class_labels_in_all[0]+" your positivle class label?")
    # Join =input("Type Y for yes and N for no.      :\n")
    # if Join == 'yes' or Join == 'Yes'or Join == 'Y'or Join == 'y' or Join == 'YES':
    #     print("You typed yes.")
    #     print(class_labels_in_all[0]+" will be modified as 1")
    #     print(os.system("for f in *csv;do sed -i -e 's#'{0}'#1#g' $f;done".format(class_labels_in_all[0])))
    #     print(os.system("for f in *csv;do sed -i -e 's#'{0}'#0#g' $f;done".format(class_labels_in_all[1])))
    #     os.system("rm *e")
    # elif Join == 'No' or Join == 'no'or Join == 'N'or Join == 'n' or Join == 'NO':
    #     print("You typed no.")
    #     print(class_labels_in_all[1] + " will be modified as 1")
    #     print(os.system("for f in *csv;do sed -i -e 's#'{0}'#1#g' $f;done".format(class_labels_in_all[1])))
    #     print(os.system("for f in *csv;do sed -i -e 's#'{0}'#0#g' $f;done".format(class_labels_in_all[0])))
    #    os.system("rm *e")


feature_preprocess("./../NB/")
feature_preprocess("./../SVM/")
feature_preprocess("./../RF/")
