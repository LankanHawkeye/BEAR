# BEAR
=======================================================


BEAR (Bootstrap and Ensemble Attribute Ranking)

=======================================================

*The BEAR program takes an input data file with attributes (features) and class labels, and applies ensemble and bootstrap strategies to select and evaluate discriminative features with respect to the class labels. Features are ranked first using five base feature selection methods (Person's correlatioin, Information Gain, Information Gain Ratio, Relief, Symmetrical Uncertainity). Then, an ensemble method is used to aggregate five base feature sets to obtain an ensemble feature set, which is evaluated using three classifiers including Naive Bayes (NB), Support Vector Machine (SVM), and Random Forest (RF). If the BEAR is used for predicting, the outcome is an ensemble prediction of the results of three classifiers. The BEAR can handle large datasets using a bootsrapping strategy. User has option to perform bootsrapping for either attributes or samples.




Installation Instructions
__________________________
1. Following are the dependencies of BEAR tool, please installl them first.
	
	1. javabridge 1.0.18
	
		Installation instructions: https://fracpete.github.io/python-weka-wrapper/install.html
	
	2. matplotlob 3.1.3
	
		Installation instructions: https://matplotlib.org/users/installing.html
	
	
	3. matplotlib-venn 0.11.5
	
		Installation instructions: https://pypi.org/project/matplotlib-venn/
		
		or https://anaconda.org/conda-forge/matplotlib-venn
		
		
	4. numpy 1.16.3
	
		Installation instructions: https://scipy.org/install.html
		
		or https://anaconda.org/anaconda/numpy
		
		
	5. pandas 1.0.1
	
		Installation instructions: https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html
	
	
	6. python-weka-wrapper 0.1.12
	
		Installation instructions: https://pypi.org/project/python-weka-wrapper/
		
		or https://fracpete.github.io/python-weka-wrapper/install.html
		
		
	7. scikit-learn 0.20.3
	
		Installation instructions: https://scikit-learn.org/stable/install.html
	
	
	8. scipy 1.2.1
		
		Installation instructions: https://www.scipy.org/install.html
		
		
	9. venn 0.1.3
		
		Installation instructions: https://pypi.org/project/venn/

2. Download the BEAR pipeline as a zipped file and unzip it to your machine.
3. cd ./BEAR_CommandLine

*Note that, user has option to run BEAR with or without bootstrapping.

	** Option 1. without bootstrapping.**
	
	 	We recommend this method for files with less than 2000 features.
		
	** Option 2. Analysing the feature file with bootstrapping.**
	
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
	
Then, user will be asked to specify the number of lines each bootstrap split should contain. To assist this decision, the script will show a table with percentages and line. Once user makes the decision and input the number, the script will create the splits and folders named after the splits. 

The script will copy the content of ./bootsrap_scripts/ folder into each newly created folder. This will create an stable  folder structure for further processing. After the running of the script, please access each newly created folders in ./pipe_step_1_Bootsrapping/ folder and run the run_pipeline.sh. This will generate feature aggregates and feature ensembles. And, each one of them will be evaulation using Naive Bayes classifier, Support Vector Machine Classifier, and Random Forest Classifier.
e.g.,
   bash ./run_pipeline.sh
