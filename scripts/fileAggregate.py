from matplotlib import pyplot as plt
from  matplotlib_venn import venn2
import pandas as pd
from os import getcwd,chdir
from glob import glob
from itertools import combinations
import sys
import os
import numpy as np


#os.chdir('/Users/miyuraj/Documents/Projects/18-Aim2/aim3/perioHealthy/BEAR-master/pipe_step_3_FAggregation/pipe_step_3_make_venn')
#currentDIR = os.getcwd()

Information_Gain = pd.read_csv('../pipe_step_3_Fselected_input/Information_Gain.csv')
Correlation = pd.read_csv('../pipe_step_3_Fselected_input/Correlation.csv')
Information_Gain_ratio = pd.read_csv('../pipe_step_3_Fselected_input/Information_Gain_Ratio.csv')
Relief = pd.read_csv('../pipe_step_3_Fselected_input/Relief.csv')
Symmetrical_Uncertainity = pd.read_csv('../pipe_step_3_Fselected_input/Symmetrical_Uncertainity.csv')

# size of the pandas
ncol = len(Information_Gain.columns)
class_index = list(Information_Gain.columns)[ncol-1]


# # # # # # #
# algorithm #
# # # # # # #
for cutoff in range(1,ncol):
    Information_Gain_List = set(Information_Gain.columns.values[0:cutoff])
    Correlation_List = set(Correlation.columns.values[0:cutoff])
    Information_Gain_ratio_List = set(Information_Gain_ratio.columns.values[0:cutoff])
    Relief_List = set(Relief.columns.values[0:cutoff])
    Information_Gain_ratio_List = set(Information_Gain_ratio.columns.values[0:cutoff])
    Symmetrical_Uncertainity_List = set(Symmetrical_Uncertainity.columns.values[0:cutoff])

    # dictionary is needed for venn diagram creation
    venn_dictionary = dict()
    venn_dictionary["Information_Gain"] = Information_Gain_List
    # print("informationGain: "+ str(Information_Gain_List))
    venn_dictionary["Correlation"] = Correlation_List
    # print("Correlation: "+ str(Correlation_List))
    venn_dictionary["Information_Gain_ratio"] = Information_Gain_ratio_List
    # print("Information_Gain_ratio: "+ str(Information_Gain_ratio_List))
    venn_dictionary["Relief"] = Relief_List
    # print("Relief: "+ str(Relief_List))
    venn_dictionary["Symmetrical_Uncertainity"] = Symmetrical_Uncertainity_List

    sets = [Information_Gain_List, Correlation_List, Information_Gain_ratio_List, Relief_List,
            Symmetrical_Uncertainity_List]
    from venn import venn
    import pandas as pd

    f_arrangement_file = open("./output_vennDiagram/feature_set_arrangement.txt", "a")
    for comboSize in range(1, len(sets) + 1):
        #print(comboSize)

        os.makedirs('../pipe_step_3_make_aggregates/'+'/at_Least.'+str(comboSize),exist_ok=True)
        #print(os.getcwd())

        ##print("combosize is "+str(comboSize))
        tempset = list()
        unitedtempset = list()
        for combo in combinations(range(len(sets)), comboSize):
            intersection = sets[combo[0]]
            for i in combo[1:]: intersection = intersection & sets[i]
            statement = " and ".join(f"Set{i + 1}" for i in combo), "=", intersection
            # print(statement)
            # f_arrangement_file.write(statement)
            f_arrangement_file.write(' '.join(str(s) for s in statement) + '\n')
            ##print("====")
            unitedtempset.append(list(intersection))
        #exit()
        # print("combosize is " + str(comboSize))
        ##print(unitedtempset)
        # make a flat list from list of lists
        flat_list = [item for sublist in unitedtempset for item in sublist]
        ##print(flat_list)
        ##print("get only uniques of flat list")
        flat_list_with_uniques = list(set(flat_list))
        # print("following is flat_list_with_uniques")
        flat_list_with_uniques.append("class")
        # print(flat_list_with_uniques)
        transposed = Information_Gain.T
        reversed = transposed.loc[flat_list_with_uniques].T
        classCol = reversed.iloc[:,-1]

        reversed.drop('class', axis=1, inplace=True)

        reversed['class'] = np.where(classCol == 'A', '1', '0')

        #print(reversed.iloc[:,-1])
        #exit()

        # need to transpose the list to be saved in csv file
        # df_list=pd.DataFrame(flat_list_with_uniques)
        ##print(df_list)
        #reversed.to_csv("../pipe_step_3_make_aggregates/at_Least.%s_" % comboSize, sep=',', index=False, header=True)
        #print(len(str(cutoff)))

        if len(str(cutoff)) < 2:
            reversed.to_csv("../pipe_step_3_make_aggregates/at_Least."+str(comboSize)+"/"+"00"+str(cutoff)+'.csv', sep=',', index=False, header=True)
        elif len(str(cutoff)) < 3:
            reversed.to_csv(
                "../pipe_step_3_make_aggregates/at_Least." + str(comboSize) + "/" + "0" + str(cutoff) + '.csv', sep=',',index=False, header=True)
        else:
            reversed.to_csv(
                "../pipe_step_3_make_aggregates/at_Least." + str(comboSize) + "/" +  str(cutoff) + '.csv', sep=',',index=False, header=True)

# get the class column
# get the x portion



