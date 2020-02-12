#cleaning any previous work
echo "Step 1 Started"
echo " "
echo "Removing Any Previous Files."
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
echo " "

echo "Clearning Complete."
echo  " "
echo "Step 1 Complete."
echo " "
echo "Run the bash script run_step_2_input_file.sh as the next step"
echo "Remember, you need to provide input file"
echo "run_step_2_input_file.sh ./input_file/example.iris.data.csv "
