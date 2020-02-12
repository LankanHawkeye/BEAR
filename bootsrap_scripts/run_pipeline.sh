#cleaning any previous work
echo "Clearning any previous files"
rm -f -v ./pipe_step_2_FS/pipe_step_2_output/*csv
rm -f -v ./pipe_step_3_FAggregation/pipe_step_3_Fselected_input/*csv
rm -f -v ./pipe_step_3_FAggregation/pipe_step_3_make_venn/output_vennDiagram/*pdf
rm -f -v ./pipe_step_3_FAggregation/pipe_step_3_make_venn/output_vennDiagram/*txt
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
echo " "
echo "Cleaning my workspace of any previous files complete."


#scp $1 ./pipe_step_2_FS/pipe_step_2_input/input.csv
#scp $1 ./pipe_step_4_clf/pipe_step_4_clf_clfers/NB/Randomized.csv
#scp $1 ./pipe_step_4_clf/pipe_step_4_clf_clfers/RF/Randomized.csv
#scp $1 ./pipe_step_4_clf/pipe_step_4_clf_clfers/SVM/Randomized.csv
# Access teh folder pipe_step_2_FS for step 2
cd ./pipe_step_2_FS/

# Run the bash script for feature selection
echo ""
echo "Feature Selection Started."
echo " "
bash ./pipe_step_2_FS.sh
echo " "
echo "Feature Selection Complete"
# Returning to working folder
cd ..

# Start the step 3

# Access the folder with step 3
cd ./pipe_step_3_FAggregation/

# Run the bash script for step 3
bash ./pipe_step_3_FA.sh
cd ..

# Accessing step 4 folder
cd ./pipe_step_4_clf/
bash ./pipe_step_4_clf.sh
cd ..

