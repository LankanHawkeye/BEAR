#Usage
#./run_bootstrapping_substep_1.sh input_file/Randomized.iris.data.2.class.csv 0.3 10 yes

mkdir -p pipe_step_1_Bootstrapping
mkdir -p pipe_step_1_Bootstrapping/input_file
mkdir -p pipe_step_1_Bootstrapping/output_feature_aggregates

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
rm -f -v ./pipe_step_1_Bootstrapping/input_file/*
rm -f -v ./pipe_step_1_Bootstrapping/output_feature_aggregates/*


/usr/local/bin/python3.7 ./scripts/Bootstrap_sampling_non_interactive.py $1 $2 $3 $4
scp $1 pipe_step_1_Bootstrapping/input_file/input.csv
