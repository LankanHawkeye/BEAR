# File created by Miyuraj Harishchandra Hikkaduwa Withanage
import glob
import os
import pandas as pd
import sys
from shutil import copyfile


# store current working directory location
curr_dir = os.getcwd()

#print(curr_dir)
#os.chdir("./pipe_step_1_Bootsrapping/input_file/")

dataset_DP2=pd.read_csv(sys.argv[1])
os.chdir(curr_dir)
# adding csv files with path to a list
# long names for copying to feature selection folder
csv_option_list_help_list=[]
# short names for menu display
csv_option_list_help_list_shortnames=[]
# Iterate through all the csv files
#print(os.getcwd())
#exit()
os.chdir('./pipe_step_1_Bootstrapping/output_feature_aggregates')
csvFiles = sorted(glob.glob('*.csv'))
for filepicker in range(0, len(csvFiles)):
    #color_count = color_count + 1
    FeatureAggrecsv = pd.read_csv(os.getcwd() + '/' + csvFiles[filepicker], delimiter=',')
    csv_option_list_help_list.append(os.getcwd() + '/' + csvFiles[filepicker])
    csv_option_list_help_list_shortnames.append(csvFiles[filepicker])
    print(str(filepicker+1)+". "+csvFiles[filepicker]+" --> " + str(FeatureAggrecsv.shape[1]-1)+" --> " +str(round(((FeatureAggrecsv.shape[1]-1)*100)/(dataset_DP2.shape[1]),2))+"%")

#os.chdir('../../')
#os.chdir('./pipe_step_2_FS/pipe_step_2_input/')
os.chdir(curr_dir)
print("")
print("-------------------------")
print("Please, choose a file from above table to be sent to feature selection: ")
chosen_file=int(input("Enter the file number of the selected file: "))
print("")
print("You picked file: "+csv_option_list_help_list_shortnames[chosen_file-1])
print("")
print("-------------------------")
copyfile(csv_option_list_help_list[chosen_file-1], './pipe_step_2_FS/pipe_step_2_input/input.csv')
copyfile(csv_option_list_help_list[chosen_file-1], './pipe_step_2_FS/pipe_step_2_input/input.csv')

print("")
print(csv_option_list_help_list[chosen_file-1] + " was copied to ./pipe_step_2_FS/pipe_step_2_input/ as input.csv")
print("")
print("Please, run the following bash script for feature selection.")
print("             bash ./run_step_2_FeatureSelection.sh")
# returning to original working folder

