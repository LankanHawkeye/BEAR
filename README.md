# BEAR
=======================================================


BEAR (Bootstrap and Ensemble Attribute Ranking)

=======================================================

The BEAR program takes an input data file with attributes (features) and class labels, and applies ensemble and bootstrap strategies to select and evaluate discriminative features with respect to the class labels. Features are ranked first using five base feature selection methods (Person's correlatioin, Information Gain, Information Gain Ratio, Relief, Symmetrical Uncertainity). Then, an ensemble method is used to aggregate five base feature sets to obtain an ensemble feature set, which is evaluated using three classifiers including Naive Bayes (NB), Support Vector Machine (SVM), and Random Forest (RF). If the BEAR is used for predicting, the outcome is an ensemble prediction of the results of three classifiers. The BEAR can handle large datasets using a bootsrapping strategy. User has option to perform bootsrapping for either attributes or samples.




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

2. Download the BEAR pipeline as a zipped file (BEAR-master.zip) and unzip it to your machine.
	
	unzip BEAR-master.zip
	
3. Access the BEAR-master folder and run Install.sh. 
	
	cd ./BEAR-master 
	
	bash ./Install.sh
	
	or
	
	sudo ./Install.sh
	
4. Place your own data to be processed in the following folder.

	Foldername:  input_file
	
	
---input data format--

The input data is essentially a comma delimited (csv) file containing features and class labels. The last column should be the class label. The header of last column should be strictly "class". Currently, only binary class labels are allowed. It is essential that class labels to be strings. All other columns are features aka attributes and their header are feature names. Identical feature names are not allowed. The values for features should be numeric. Since we are using Naive Bayes classifier, it is important that values are non-negative.

A sample input data file "Randomized.iris.data.2.class.csv" can be found in "input_file" folder.

Note that, user has option to run BEAR with or without bootstrapping.

**Option 1: run BEAR without bootstrapping**

5. Run the "run_step_1_and_2_fs_without_bootstrapping.sh" bash along with an input file as the first argument.
   This step will copy the input file into necessary processing folders, and then perform feature selection. Five base feature selection methods will be used, including 1. Pearson's correlation, 2. Information Gain, 3. Information Gain Ratio, 4. Relief, and 5. Symmetrical Uncertainity. The output will be new reordered datasets according to feature rankings. The output will be available in folder "pipe_step_2_FS/pipe_step_2_output". This step will also prepare rquuired files for further processing by copying the reordered output files into other necessary folders.
   
Here is a command to run feature selection on sample input file "Randomized.iris.data.2.class.csv":

	bash ./run_pipeline.sh input_file/Randomized.iris.data.2.class.csv

6. Run the "run_step_3_vennDiFeAEns_without_bootstrapping.sh".
   This script allows user to pick top n features for each base feature selection method by specifying a numeric argument. 
   Then, five sets of top n features will be used for Venn diagrams, feature aggregation, and feature ensemble.
   
   For example, following script picks top 30 ranked features:
   
   	bash ./run_step_3_vennDiFeAEns_without_bootstrapping.sh 30
   
7. Run "run_step_4_clfEvaluation_without_bootstrapping.sh". This step evaluates all picked feature sets from step 6, which is obtained based on the classification performance measured by the area under curve (AUC) value of the classification ROC curve. Three classifiers (NB, SVM, and RF) with default parameter set are used. More advanced users can modify the parameter sets of these classifiers by editing their corresponding python scripts.

Here is a sample code for stet 7:

	bash ./run_step_4_clfEvaluation_without_bootstrapping.s	

8. Run "run_step_5_barplots_without_bootstrapping.sh" to generate bar plots of selected AUC values:

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

Once finising step 8, **Running bash ./run_step_0_clean.sh** to remove the results in the folder (Recomended when user has copied all the results to his/her own folders and is ready to perform a new analysis).


**Option 2: run BEAR with bootstrapping**

1. To run BEAR with bootstrapping, you must run the script run_bootstrapping_substep_1.sh. This script takes 4 commandline arguments.

   argument 1 = input csv file.
   
   argument 2 = Sampling Fraction: Fraction of the features to be used. This should strictly be a value between 0 and 1. It can be 1 as   well. 
   
   argument 3 = Number of bootstrap samples to draw from data file. This value should strictly be integer.
   
   argument 4 = This argument should be specified as yes or no. Here, user has the chance to specify the positive class. If you provide yes as the fourth argument, it will assign one of the class labels as positive class and the other one as the negative one. If you provided no as the argument, the opposite will happen. Use will be displayed which class was assigned as positive class. 
   
   e.g., 
   
   	bash ./run_bootstrapping_substep_1.sh input_file/Randomized.iris.data.2.class.csv 0.3 10 yes
	
	During execution of the script, user will be shown some useful information.
	1. Number of features in input file.
	2. Number of samples in input file.
	3. User-specified sampling fraction.
	4. User-specified number of bootstrap samples.
	5. The class labels.
	6. positive class label (indicated as 1).
	7. Table of feature aggregates created as a result of bootstrapping.
		This table contains the number of features each aggregate contains. The same information will be shown as percentage.
		This is to help the user to pick the optimum aggregate user wants to further investigate.
	At the end of the execution of this script, user will be asked to run the next script.
	
2. In this step, user need to provide the file to be used to further processing. User should run the bash script named ./run_bootstrapping_substep_2.sh. Then, the program will prompt user an enumerated menu of file aggregates created. User has to select the number from the table and hit enter. This will copy the chosen file to the folder next up for processing.

e.g., 
	bash ./run_bootstrapping_substep_2.sh
	
3. Next Step is to run the feature selection. Please, follow the above procedure from Feature selection.
