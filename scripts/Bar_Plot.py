

import matplotlib.pyplot as plt;plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import sys
import re
import os


# global variable of top selected numbers
top = 1


def create_bar_plot(top,path,filename_variable):
    os.chdir(path)
    filepath = filename_variable
    NAMECLF = str(filepath).replace('_AUC.txt', '')
    print("Generating Bar Charts for " + NAMECLF + " Started.")
    # filepath = 'ComplementNB_AUC.txt'
    cnt = 0
    # We have to read the file and extract out the information
    filename_list = []

    # Created an empty dictionary
    # The file names will be keys
    # Lists of AUC will be values

    mydictionary = dict()
    with open(filepath) as fp:
        for line in fp:
            cnt = cnt + 1
            # File names are in odd numbered lines
            if cnt % 2 == 1:
                withoutCSV = line.replace('.csv\n', '')
                filename_list.append(withoutCSV)
                # print(withoutCSV)

            else:
                # AUC lists are in even numbered lines
                raw_AUC = line
                k2 = raw_AUC.replace('[', '')
                k3 = k2.replace(']\n', '')
                k4 = k3.replace('\n', '')
                # define cleaned list with zero as first element
                # The reason is first one's index is zero

                cleaned_list = k4.split(sep=",")

                mydictionary[withoutCSV] = cleaned_list

    colors = ['red', 'navy', 'orange', 'dodgerblue', 'magenta', 'brown', 'purple', 'green', 'gold', 'lawngreen', 'aqua']
    import re
    # AUC_list will store the respective AUC values for bar chart

    # displaying the sizes of each file name
    # this is required when deciding the top value
    # it is important to output the monimum value
    #length_list = []
    # print("===============================")
    # print("Following table shows the file names and the number of AUC values stored in them")
    # print("Please, review them and pick the AUC value that is equal to or the minimum number.")
    # print("===============================")
    # print("")
    # for f in filename_list:
    #     print(f, end=" ")
    #     print("---->", end=" ")
    #     print(len(mydictionary.get(f)))

    # Identifying the maximum number that can be placed
    #max_length_list = []
    #for f in filename_list:
    #    max_length_list.append(len(mydictionary.get(f)))

    #print("")
    #print("-------------------------------")
    #print("Allowed top number of features is : " + str(min(max_length_list)) + ". Please, refer to the above information to retriev the limiting file name")
    #print(
    #    "Please, type in the top number of features (i.e., selected number of featuers) according to above guidelines.")
    #Join = input("Type top number of features      :\n")
    # if int(Join) == min(max_length_list) or int(Join) <= min(max_length_list) and int(Join) > 0:
    #     print("You typed " + Join)
    AUC_list = []
    # Negative ne is added because list start at zero index
    #top = int(Join) - 1
    for f in filename_list:
        # print(f)
        AUC_list.append(mydictionary.get(f)[top])
        # print(AUC_list)

    y_position = np.arange(len(filename_list))

    # AUC list I am getting is like this ['33','54','67']
    # If I don't remove the quotation markes, this won't work properly
    # it should be [33,54,67]
    #  Following statement will convert them to numerical list
    AUC_list = [float(value) for value in AUC_list]

    plt.figure(figsize=(7, 7))
    plt.bar(np.asarray(y_position), np.asarray(AUC_list), width=0.4, alpha=1, color=colors, label=filename_list)
    # plt.xlim(0,len(xaxis))
    plt.ylim(0, 1.1)
    plt.ylabel('AUC')
    plt.xticks(y_position, filename_list)
    # plt.legend((p1[0], p2[0]), ('Men', 'Women'))

    # print(NAMECLF)
    plt.title(NAMECLF + ' - Bar Chart of AUC Values for top ' + str(top) + ' features')
    plt.tick_params(labelsize=5)
    plt.xticks(rotation=20)
    # plt.legend(loc='best')
    plt.savefig("../result_bar_plots/" + NAMECLF + "_Barplot_AUC.pdf")

    print("Generating Bar Charts for " + NAMECLF + " Complete.")
    fp.close()

def checking_feature_numbers(path,filename_fixed):
    os.chdir(path)
    filepath = filename_fixed
    #NAMECLF = str(filepath).replace('_AUC.txt', '')
    print("Checking Allowed Feature Number for Generating Bar Charts Started.")
    # filepath = 'ComplementNB_AUC.txt'
    cnt = 0
    # We have to read the file and extract out the information
    filename_list = []

    # Created an empty dictionary
    # The file names will be keys
    # Lists of AUC will be values

    mydictionary = dict()
    with open(filepath) as fp:
        for line in fp:
            cnt = cnt + 1
            # File names are in odd numbered lines
            if cnt % 2 == 1:
                withoutCSV = line.replace('.csv\n', '')
                filename_list.append(withoutCSV)
                # print(withoutCSV)

            else:
                # AUC lists are in even numbered lines
                raw_AUC = line
                k2 = raw_AUC.replace('[', '')
                k3 = k2.replace(']\n', '')
                k4 = k3.replace('\n', '')
                # define cleaned list with zero as first element
                # The reason is first one's index is zero

                cleaned_list = k4.split(sep=",")

                mydictionary[withoutCSV] = cleaned_list

    #colors = ['red', 'navy', 'orange', 'dodgerblue', 'magenta', 'brown', 'purple', 'green', 'gold', 'lawngreen', 'aqua']
    import re
    # AUC_list will store the respective AUC values for bar chart

    # displaying the sizes of each file name
    # this is required when deciding the top value
    # it is important to output the monimum value
    length_list = []
    print("===============================")
    print("Following table shows the file names and the number of AUC values stored in them")
    print("Please, review them and pick the AUC value that is equal to or the minimum number.")
    print("===============================")
    print("")
    for f in filename_list:
        print(f, end=" ")
        print("---->", end=" ")
        print(len(mydictionary.get(f)))

    # Identifying the maximum number that can be placed
    max_length_list = []
    for f in filename_list:
        max_length_list.append(len(mydictionary.get(f)))

    print("")
    print("-------------------------------")
    print("Allowed top number of features is : " + str(
        min(max_length_list)) + ". Please, refer to the above information to retrieve the limiting file name")
    print(
        "Please, type in the top number of features (i.e., selected number of featuers) according to above guidelines.")
    Join = input("Type top number of features      :\n")
    if int(Join) == min(max_length_list) or int(Join) <= min(max_length_list) and int(Join) > 0:
        print("You typed " + Join)
        AUC_list = []
        # Negative ne is added because list start at zero index
        #top = int(Join) - 1
        top = int(Join)
        create_bar_plot(top,'.', 'ComplementNB_AUC.txt')
        create_bar_plot(top,'.', 'RF_AUC.txt')
        create_bar_plot(top,'.', 'SVM_AUC.txt')
        return top
    else:
        print("Please, input a valid number of top features. Review above guideleines and re-run the program.")
        fp.close()
        exit()


checking_feature_numbers('.','ComplementNB_AUC.txt')
#create_bar_plot('.','ComplementNB_AUC.txt')
#create_bar_plot('.','RF_AUC.txt')
#create_bar_plot('.','SVM_AUC.txt')