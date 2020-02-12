#cleaning any previous work
echo "Clearning any previous files"
rm -f -v ./pipe_step_2_FS/pipe_step_2_output/*csv
rm -f -v ./pipe_step_3_FAggregation/pipe_step_3_Fselected_input/*csv
rm -f -v ./pipe_step_3_FAggregation/pipe_step_3_make_venn/output_vennDiagram/*pdf
rm -f -v ./pipe_step_3_FAggregation/pipe_step_3_make_ensemble/ensemble_output/*csv
rm -f -v ./pipe_step_3_FAggregation/pipe_step_3_make_aggregates/*csv
rm -f -v ./pipe_step_4_clf/pipe_step_4_clf_clfers/NB/*csv
rm -f -v ./pipe_step_4_clf/pipe_step_4_clf_clfers/NB/*pdf
rm -f -v ./pipe_step_4_clf/pipe_step_4_clf_clfers/NB/*txt
rm -f -v ./pipe_step_4_clf/pipe_step_4_clf_clfers/SVM/*csv
rm -f -v ./pipe_step_4_clf/pipe_step_4_clf_clfers/SVM/*pdf
rm -f -v ./pipe_step_4_clf/pipe_step_4_clf_clfers/SVM/*txt
rm -f -v ./pipe_step_4_clf/pipe_step_4_clf_clfers/RF/*csv
rm -f -v ./pipe_step_4_clf/pipe_step_4_clf_clfers/RF/*pdf
rm -f -v ./pipe_step_4_clf/pipe_step_4_clf_clfers/RF/*txt
rm -f -v ./pipe_step_4_clf/result_auc_for_each_position/*txt
rm -f -v ./pipe_step_4_clf/result_bar_plots/*pdf
rm -f -v ./pipe_step_4_clf/result_classifier_evalutions/*pdf

scp $1 ./pipe_step_2_FS/pipe_step_2_input/input.csv

# Access teh folder pipe_step_2_FS for step 2
cd ./pipe_step_2_FS/

# Run the bash script for feature selection
bash ./pipe_step_2_FS.sh

# Returning to wroking folder
cd ..

# Start the step 3

# Access the folder with step 3
cd ./pipe_step_3_FAggregation/

# Run the bash script for step 3
bash ./pipe_step_3_FA.sh $2
cd ..

# Accessing step 4 folder
cd ./pipe_step_4_clf/
bash ./pipe_step_4_clf.sh
cd ..

# Generating Bar charts

cd ./pipe_step_4_clf/result_auc_for_each_position/
/usr/local/bin/python3.7 Bar_Plot.py ComplementNB_AUC.txt
/usr/local/bin/python3.7 Bar_Plot.py RF_AUC.txt
/usr/local/bin/python3.7 Bar_Plot.py SVM_AUC.txt
cd ../..
