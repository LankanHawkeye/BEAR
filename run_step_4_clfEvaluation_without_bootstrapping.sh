# Accessing step 4 folder
cd ./pipe_step_4_clf/pipe_step_4_clf_clfers/preprocess_script/
# Following three preprocessing steps are required before classifier action
/usr/local/bin/python3.7 preprocess_class_labels_for_classifiers.py

cd ../../
cd ./pipe_step_4_clf_clfers/NB/
echo "starting classifiers. 1. NB, 2. SVM, 3.RF"
# classifier action
/usr/local/bin/python3.7 NaiveBayes.py

cd ../../
cd ./pipe_step_4_clf_clfers/SVM/

/usr/local/bin/python3.7 SVM_StratKfold3_gammaSuto_rbf.py

cd ../../
cd ./pipe_step_4_clf_clfers/RF/
/usr/local/bin/python3.7 RandomForest_classifier_allfiles.py


echo ""
echo ""
echo "========================"
echo "Classifier Evaulation Complete"
echo ""
echo "Please, run the following script to get bar plots"
echo "bash ./run_step_5_barplots_without_bootstrapping.sh"
