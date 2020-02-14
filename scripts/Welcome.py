# Created by Miyuraj Harishchandra Hikkaduwa WIthanage

import os
import pandas as pd
import glob
from shutil import copyfile

print("=================================================================")
print("")
print("         BEAR (Bootstrap and Ensemble Attribute Ranking)         ")
print("")
print("=================================================================")
print("")
print("")
print("The BEAR program takes an input data file with attributes (features) \nand class labels, and applies ensemble and bootstrap strategies to \nselect and evaluate discriminative features with respect to the class \nlabels. Features are ranked first using five base feature selection \nmethods (Person's correlatioin, Information Gain, Information Gain Ratio, \nRelief, Symmetrical Uncertainity). Then, an ensemble method is used to \naggregate five base feature sets to obtain an ensemble feature set, \nwhich is evaluated using three classifiers including Naive Bayes (NB), \nSupport Vector Machine (SVM), and Random Forest (RF). If the BEAR is \nused for predicting, the outcome is an ensemble prediction of the results \nof three classifiers. The BEAR can handle large datasets using \na bootsrapping strategy. User has option to perform bootsrapping \nfor either attributes or samples.")
print("")
print("")
print("Welcome to BEAR!!!")
print("")
print("")
print("Note that, user has two options (modes) when it comes to running BEAR")
print("")
print("--------------------------------------------------------------")
print("1: run BEAR without bootstrapping")
print("2: run BEAR with bootstrapping")
print("--------------------------------------------------------------")
print("")
print("Please, choose your option below.")
print("")
option1=int(input("Enter the option number from above table here: "))
print("")
if option1 == 1:
    print("You have selection the option 1: run BEAR without bootstrapping.")
    print("Following are the csv files in your input_file folder")
    print("-------------------------------------------------")
    currentwd = os.getcwd()
    #print(currentwd)


    # long names for copying to feature selection folder
    csv_option_list_help_list = []
    # short names for menu display
    csv_option_list_help_list_shortnames = []
    # Iterate through all the csv files
    os.chdir(currentwd + '/input_file/')



    csvFiles = sorted(glob.glob('*.csv'))
    for filepicker in range(0, len(csvFiles)):
        # color_count = color_count + 1
        FeatureAggrecsv = pd.read_csv(os.getcwd() + '/' + csvFiles[filepicker], delimiter=',')
        csv_option_list_help_list.append(os.getcwd() + '/' + csvFiles[filepicker])
        csv_option_list_help_list_shortnames.append(csvFiles[filepicker])
        # Displays the list of csv files in input folder
        print(str(filepicker + 1) + ". " + csvFiles[filepicker])

    os.chdir('../pipe_step_2_FS/pipe_step_2_input/')


    destination_dir = os.getcwd()
    destination_file = destination_dir + "/input.csv"
    #print(destination_dir)

    print("-------------------------")
    print("Please, choose a file from above list to start BEAR: ")
    chosen_file = int(input("Enter the file number of the selected file: "))
    print("")

    print("You picked file: " + csv_option_list_help_list_shortnames[chosen_file - 1])
    selected_file = csv_option_list_help_list[chosen_file - 1]
    # print(csv_option_list_help_list[chosen_file - 1] + " was copied to ./pipe_step_2_FS/pipe_step_2_input/ as input.csv")

    # print(destination_file)
    # (csv_option_list_help_list[chosen_file - 1], str(str(current)+"/pipe_step_1_Bootstrapping/input_file/input.csv"))
    # To copy the file, I had to chdir to the destination directory
    # otherwise, it will not copy
    os.system("scp {0} {1}".format(str(csv_option_list_help_list[chosen_file - 1]), destination_file))
    print("Next Step is to run the feature selection. ")
    print("Please, follow the option 1 (run BEAR without bootstrapping) pipeline from step 6 (See https://github.com/biocoms/BEAR/blob/master/README.md)")
    print("6.run_step_2_FeatureSelection.sh")
    print("Example: bash ./run_step_2_FeatureSelection.sh")
    exit()

elif option1 == 2:
    print("You have selection the option 2: run BEAR with bootstrapping.")
    print("")
    print("Following are the csv files in your input_file folder")
    print("-------------------------------------------------")
    currentwd = os.getcwd()

    # long names for copying to feature selection folder
    csv_option_list_help_list = []
    # short names for menu display
    csv_option_list_help_list_shortnames = []
    # Iterate through all the csv files
    os.chdir(currentwd+'/input_file/')
    

    csvFiles = sorted(glob.glob('*.csv'))
    for filepicker in range(0, len(csvFiles)):
        # color_count = color_count + 1
        FeatureAggrecsv = pd.read_csv(os.getcwd() + '/' + csvFiles[filepicker], delimiter=',')
        csv_option_list_help_list.append(os.getcwd() + '/' + csvFiles[filepicker])
        csv_option_list_help_list_shortnames.append(csvFiles[filepicker])
        # Displays the list of csv files in input folder
        print(str(filepicker + 1) + ". " + csvFiles[filepicker])

    os.chdir(currentwd+'/pipe_step_1_Bootstrapping/input_file/')
    destination_dir=os.getcwd()
    destination_file=destination_dir+"/input.csv"
    print(destination_dir)

    print("-------------------------")
    print("Please, choose a file from above list to start BEAR: ")
    chosen_file = int(input("Enter the file number of the selected file: "))
    print("")

    print("You picked file: " + csv_option_list_help_list_shortnames[chosen_file - 1])
    selected_file = csv_option_list_help_list[chosen_file - 1]
    #print(csv_option_list_help_list[chosen_file - 1] + " was copied to ./pipe_step_2_FS/pipe_step_2_input/ as input.csv")


    #print(destination_file)
    #(csv_option_list_help_list[chosen_file - 1], str(str(current)+"/pipe_step_1_Bootstrapping/input_file/input.csv"))
    # To copy the file, I had to chdir to the destination directory
    # otherwise, it will not copy
    os.system("scp {0} {1}".format(str(csv_option_list_help_list[chosen_file - 1]),destination_file))

    import Bootstrap_sampling
    exec('Bootstrap_sampling')

    print("Next Step is to run the feature selection. ")
    print(
        "Please, follow the option 1 (run BEAR without bootstrapping) pipeline from step 6 (See https://github.com/biocoms/BEAR/blob/master/README.md)")
    print("6.run_step_2_FeatureSelection.sh")
    print("Example: bash ./run_step_2_FeatureSelection.sh")
    exit()

else:
    print("You did not enter a valid option.")
    print("Program will exit. Please, re-run it with a valid option")
    exit()

