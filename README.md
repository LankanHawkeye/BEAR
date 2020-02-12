# BEAR
=======================================================


BEAR (Bootstrap and Ensemble Attribute Ranking)

=======================================================

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


5. Run the "run_pipeline.sh" bash along with giving input file as the first argument.
   See the example.
	e.g., We have provided you an example data set called "Randomized.iris.data.2.class.csv".
     	      You will find it in the folder ./input_file/
	      Run the bash script following the example. 
	      The number 3 at the end is a threshold value you need to provide.
	      It is the top features you want to consider for investigation.
	      That number has to be strictly below the total number of features. 

bash ./run_pipeline.sh input_file/Randomized.iris.data.2.class.csv 3

6. Please, note that during the time program run, the program will notify you when it attempts to
   convert the string class labels to numeric class labels.
   It will ask you to select the positive class label in the form of a question.
   If your answer is yes, then type y and press enter key.
   If you want the other class label to be the positive class, then type n and press enter key.


7. You will find different output files in different folders of this tool. 

8. How to input the number of top-selected features for further investigation?
   You have to provide a value that is less than the total number of features being considered.   
   This value is given as the third argument of the following.      |
	bash ./run_pipeline.sh input_file/Randomized.iris.data.2.class.csv 3 <--
