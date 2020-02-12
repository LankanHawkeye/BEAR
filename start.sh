#!/bin/bash
# Bash Menu Script Example


echo "============================"
echo "      M2ROC                 "
echo "==========================="

echo " "

echo "Welcome to M2ROC tool"


echo "Here are some of the essential tips"
echo "---input file format--"
echo "Input file is essentially a comma delimited file csv file."
echo "It should contain features / sttributes and class labels."
echo "class label column should be the last column of the csv file."

echo "The heade of class label should be strictly class."
echo "The class labels should only be binary."
echo "It is essential that class labels to be strings."
echo "All other columns are features aka attributes. "
echo "The header are feature names."
echo "Header names should be unique."
echo "The values can only be numeric .Since we are using Naive Bayes classifier, it is important that values are non-negative."
echo " "
echo "An example input csv file is shown below, within dashed lines."
echo " "
echo "-------------------------------------"
echo "attrib1  attrib2 .. attrib_n  class     <-- header line contains features/attributes and class	"
echo "10	 34	 .. 21	      Treatment "
echo "23	 24	 .. 23        Treatment "
echo "34	 56	 .. 54        Treatment "
echo "45	 21	 .. 23        Control "
echo "54	 87	 .. 11        Control "
echo "32 	 23	 .. 23	      Control "
echo "-------------------------------------- "
echo " "
echo " "




PS3='Please enter your choice: '
options=("1. Run M2ROC without bootsrap" "2. Run M2ROC with bootsrap" "3. Quit")
#options=("Option 1" "Option 2"  "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "1. Run M2ROC without bootsrap")
            echo "You chose to run M2ROC WITHOUT bootsrapping."
            ;;
        "2. Run M2ROC with bootsrap")
            echo "You chose to run M2ROC WITH bootsrapping"
	    echo "Please, run the script run_pipeline.sh followingg the guidelines in README.txt file"
	    break
            ;;
        "3. Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
