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

One finising step 8, **Running bash ./run_step_0_clean.sh** to remove the results in the folder (Recomended when user has copied all the results to his/her own folders and is ready to perform a new analysis).


**Option 2: run BEAR with bootstrapping**

First, run feature selection with bootstrapping:

	bash ./with_bootsrap_run_pipeline.sh ./input_file/Randomized.iris.data.2.class.csv
	
Then, user has to specify the sample size of each of bootstrapped sample subsets. The bootstrapped sample subsets are generated and stored in subfolders of ./bootsrap_scripts/. Please access to each newly created subfolder in ./pipe_step_1_Bootsrapping/ folder and run the run_pipeline.sh. This will generate feature aggregates and feature ensembles. And, each feature set will be evaulated based on the classification performance measured by the area under curve (AUC) value of the classification ROC curve. Three classifiers (NB, SVM, and RF) with default parameter set are used:

	bash ./run_pipeline.sh
