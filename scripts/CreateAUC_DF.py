# importing  a script with two functions
import NB_SVM_functions as myModule
import pandas as pd
import os

# Defining the dataframe to which we get AUC values
df = pd.DataFrame()
df = pd.read_csv('../../pipe_step_4_clf/result_auc_for_each_position/ComplementNB_AUC.csv', delimiter=',',header=0)

workingDir = os.getcwd()

#####
# NB
#####



atleast1_NB=myModule.functionNB('at_Least.1')
os.chdir(workingDir)
atleast2_NB=myModule.functionNB('at_Least.2')
os.chdir(workingDir)
atleast3_NB=myModule.functionNB('at_Least.3')
os.chdir(workingDir)
atleast4_NB=myModule.functionNB('at_Least.4')
os.chdir(workingDir)
atleast5_NB=myModule.functionNB('at_Least.5')
os.chdir(workingDir)

df['atLeast1_NB'] = atleast1_NB
df['atLeast2_NB'] = atleast2_NB
df['atLeast3_NB'] = atleast3_NB
df['atLeast4_NB'] = atleast4_NB
df['atLeast5_NB'] = atleast5_NB


#####
# SVM
#####
df_SVM = pd.read_csv('../../pipe_step_4_clf/result_auc_for_each_position/SVM_AUC.csv', delimiter=',',header=0)
frames = [df, df_SVM]
df = pd.concat(frames,axis=1)

atleast1_SVM=myModule.functionSVM('at_Least.1')
os.chdir(workingDir)
atleast2_SVM=myModule.functionSVM('at_Least.2')
os.chdir(workingDir)
atleast3_SVM=myModule.functionSVM('at_Least.3')
os.chdir(workingDir)
atleast4_SVM=myModule.functionSVM('at_Least.4')
os.chdir(workingDir)
atleast5_SVM=myModule.functionSVM('at_Least.5')
os.chdir(workingDir)

df['atLeast1_SVM'] = atleast1_SVM
df['atLeast2_SVM'] = atleast2_SVM
df['atLeast3_SVM'] = atleast3_SVM
df['atLeast4_SVM'] = atleast4_SVM
df['atLeast5_SVM'] = atleast5_SVM



df.to_csv('./atleast_summary.csv',sep=',',index=False,header=True)
