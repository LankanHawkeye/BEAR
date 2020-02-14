
# -*- coding: utf-8 -*-
print("Symmetrical Uncertainity Feature Selection Started.")
import sys
input_file=sys.argv[1]
output_file=sys.argv[2]
import csv
import pandas as pd
import weka.core.jvm as jvm
from weka.core.converters import Loader, Saver
#jvm.start(system_cp=True, packages=True)
#need to give the weka installation location
jvm.start(packages="/anaconda3/lib/python3.7/site-packages/weka/")
from weka.attribute_selection import ASSearch, ASEvaluation, AttributeSelection
loader = Loader(classname="weka.core.converters.CSVLoader")
dataset_DP2 = pd.read_csv(input_file)
data = loader.load_file(input_file)
#print(data)
search = ASSearch(classname="weka.attributeSelection.Ranker",options=["-N", "-1"])
#evaluator = ASEvaluation(classname="weka.attributeSelection.CfsSubsetEval", options=["-T", "1.797", "-N", "-1"])
evaluator = ASEvaluation("weka.attributeSelection.SymmetricalUncertAttributeEval", options=[])
attsel = AttributeSelection()
attsel.ranking(True)
attsel.search(search)
attsel.evaluator(evaluator)
attsel.select_attributes(data)
#print("# attributes: " + str(attsel.number_attributes_selected))
#print("attributes: " + str(attsel.selected_attributes))
#Selects the attribute columns discarding gthe class column
#print(str(attsel.selected_attributes[0:len(attsel.selected_attributes)-1]))
# getting name of attribute data.attribute(0).name
#print(dataset_DP2.T)

sorted_feature_list=[]
#creating list of names
for position in range(0,len(attsel.selected_attributes)):
    sorted_feature_list.append(data.attribute(attsel.selected_attributes[position]).name)
    #print(data.attribute(attsel.selected_attributes[position]).name)
    #print(position)

#print(sorted_feature_list)

transposed = dataset_DP2.T
hashing_dictionary = dict()
##print(data.attribute(0).name)
#print(transposed.loc[sorted_feature_list])
reversed = transposed.loc[sorted_feature_list].T
reversed = reversed.sample(frac=1)
#print(reversed)
reversed.to_csv(output_file+ "%s.csv" % "Symmetrical_Uncertainity", sep=',',  index=False)
print("Symmetrical Uncertainity Feature Selection Complete.")
jvm.stop()
