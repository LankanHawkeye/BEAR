# BEAR
=======================================================


BEAR (Bootstrap and Ensemble Attribute Ranking)

=======================================================
*This program will take a data file with attributes (features), their abundances and binary class labels, and pick top important attributes with respect to the class labels. This program will rank the features using five attribute selection programs (Person's correlatioin, Information Gain, Information Gain Ratio, Relief, Symmetrical Uncertainity). Then, it will use an in-house script to re-rank the attributes based on our ensemble scoring function. The program will evaluate the ranking of the features with Naive Bayes classifier, Support Vector Machine Classifier, and Random Forest Classifier. This program will handle large datasets using a bootsrapping strategy.* 


Installation Instructions
.................
1. Install following dependencies first.



	Following are the dependencies of BEAR tool.
	1. javabridge
	2. matplotlob
	3. matplotlib-venn
	4. numpy
	5. pandas
	6. python-weka-wrapper
	7. scikit-learn
	8. scipy
	9. sklearn
	10. venn

2. Unzip the zipped file.
3. cd ./BEAR_CommandLine

*Note that, user can choose to execute two analysis pathways.
	**1. Analysing the feature file without bootstrapping.**
	 	We recommend this method for files with less than 2000 features.
	**2. Analysing the feature file with bootstrapping.**
		We recommend this method for files with larger number of features.*

**Analysing the feature file without bootstrapping.**
4. Place, the input file to be processed in the following folder.
	Foldername:  input_file
---input file format--
Input file is essentially a comma delimited file (csv) file.
It should contain features (attributes) and class labels.
class label column should be the last column of the csv file.
The header of class label should be strictly "class".
The class labels should only be binary.
It is essential that class labels to be strings (i.e., two strings).
All other columns are features aka attributes. 
The header are feature names.
Header names should be unique.
The values can only be numeric (Obvious point).Since we are using Naive Bayes classifier, it is important that values are non-negative.


5. Run the "run_step_1_and_2_fs_without_bootstrapping.sh" bash along with giving input file as the first argument.
   See the example. This step will copy the input file into necessary processing folders.
   And, the script will rank the input features according to their inportance.
   We are using 5 feature selection methods: 1. Pearson's correlation, 2. Information Gain, 3. Information Gain Ratio, 4. Relief,  5.     Symmetrical Uncertainity. The output will be new reordered datasets according to feature rankings. The output will be available in ./ pipe_step_2_FS/pipe_step_2_output/. This script will further copy the reordered output files into other folders for further processing.
   
	e.g., We have provided you an example data set called "Randomized.iris.data.2.class.csv".
     	      You will find it in the folder ./input_file/
	      Run the bash script following the example. 
	      
e.g.,
bash ./run_pipeline.sh input_file/Randomized.iris.data.2.class.csv

6. Next step is running "run_step_3_vennDiFeAEns_without_bootstrapping.sh".
   This script takes a numeric argument. User should provide the top number of features ranked to be investigated.
   Then, only those ranked features will be considered for creating Venn diagrams, feature aggregates, and feature ensemble.
   Feature ensemble uses a scoring function dependent on all used feature selection methods. 
   e.g.,
   Assuming user is interested in top 30 ranked features,
   bash ./run_step_3_vennDiFeAEns_without_bootstrapping.sh 30
   
7. Next step is running "run_step_4_clfEvaluation_without_bootstrapping.sh". This step will convert the string class labels into numeric       binary labels. After, that it will evaluation all newly created re-ordered feature files. We are basically checking which order is going    to give us the best result. We pick the best result based on Area Under Curve (AUC) value of ROC curve. If there is a files with n number of features, the script will evaluate from position 1 to n, increamenting by 1. At each increment, program will evaluate and return an AUC value. For evaluation, we have used Complement Naive Bayes classifier, Random Forest Classifier, and Support Vector Machine classifier. A more advanced user can modify the parameter's of these classifiers by editing those python scripts.
e.g.,
	bash ./run_step_4_clfEvaluation_without_bootstrapping.s	

8. Final, step is to generate bar plots of selected AUC values. 
e.g.,
	bash ./run_step_5_barplots_without_bootstrapping.sh
	
*Output file locations*
*=====================*

Feature Ranked input files
./pipe_step_2_FS/pipe_step_2_output/

Venn Diagrams and Ranked Feature Combinations
./pipe_step_3_FAggregation/pipe_step_3_make_venn/output_vennDiagram/

Feature Ensemble Generated Using Scoring Function
./pipe_step_3_FAggregation/pipe_step_3_make_ensemble/ensemble_output/

Ranked Feature Combinations
./pipe_step_3_FAggregation/pipe_step_3_make_aggregates/

Ranked Feature Sets - Evaluations Using Classifiers
./pipe_step_4_clf/result_classifier_evalutions/

Ranked Feature Sets - Calculated AUC Values (For Each Ranked Position) in Text Files
./pipe_step_4_clf/result_auc_for_each_position/"

Bar Plots
./pipe_step_4_clf/result_bar_plots/

**Running bash ./run_step_0_clean.sh** will remove the results in the folder (Recomended to use when you have copied the results to your own folders and ready to perform a new analysis).

	
**Analysing the feature file with bootstrapping.**
This analysis path is selected only when the input file contains a large number of features (>2000). To follow this path, user should run the script with_bootsrap_run_pipeline.sh specifying an input.csv as the first argument.
First of all, place your input file in folder ./input_file/.
Make sure to rename it as input.csv.

Next, run,
	bash ./with_bootsrap_run_pipeline.sh ./input_file/input.csv
	
Then, user will be asked to specify the number of lines (i.e., rows or observations) each bootstrap split should contain. To assist this decision, the script will show a table with percentages and line. Once user makes the decision and input the number, the script will create the splits and folders named after the splits. 

The script will copy the content of ./bootsrap_scripts/ folder into each newly created folder. This will create an stable  folder structure for further processing. After the running of the script, please access each newlyc created folder in ./pipe_step_1_Bootsrapping/ folder and run the run_pipeline.sh.
e.g.,
   bash ./run_pipeline.sh
