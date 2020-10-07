mkdir -p ./configuration
mkdir -p ./pipe_step_1_Bootstrapping
mkdir -p ./pipe_step_1_Bootstrapping/input_file
mkdir -p ./pipe_step_1_Bootstrapping/output_feature_aggregates
mkdir -p ./pipe_step_2_FS
mkdir -p ./pipe_step_2_FS/pipe_step_2_input
mkdir -p ./pipe_step_2_FS/pipe_step_2_scripts
mkdir -p ./pipe_step_2_FS/pipe_step_2_output
mkdir -p ./pipe_step_3_FAggregation
mkdir -p ./pipe_step_3_FAggregation/pipe_step_3_make_ensemble
mkdir -p ./pipe_step_3_FAggregation/pipe_step_3_make_ensemble/ensemble_output
mkdir -p ./pipe_step_3_FAggregation/pipe_step_3_make_venn
mkdir -p ./pipe_step_3_FAggregation/pipe_step_3_make_venn/output_vennDiagram
mkdir -p ./pipe_step_3_FAggregation/pipe_step_3_Fselected_input
mkdir -p ./pipe_step_3_FAggregation/pipe_step_3_make_aggregates
mkdir -p ./pipe_step_4_clf
mkdir -p ./pipe_step_4_clf/result_bar_plots
mkdir -p ./pipe_step_4_clf/pipe_step_4_clf_clfers
mkdir -p ./pipe_step_4_clf/pipe_step_4_clf_clfers/RF
mkdir -p ./pipe_step_4_clf/pipe_step_4_clf_clfers/SVM
mkdir -p ./pipe_step_4_clf/pipe_step_4_clf_clfers/preprocess_script
mkdir -p ./pipe_step_4_clf/pipe_step_4_clf_clfers/NB
mkdir -p ./pipe_step_4_clf/result_auc_for_each_position
mkdir -p ./pipe_step_4_clf/result_classifier_evalutions

scp ./scripts/configuration.py ./configuration/configuration.py
scp ./scripts/configuration.py ./pipe_step_2_FS/pipe_step_2_scripts/configuration.py

scp ./scripts/Correlation_Fselection.py ./pipe_step_2_FS/pipe_step_2_scripts/Correlation_Fselection.py
scp ./scripts/SymmetricalUncert_Fselection.py ./pipe_step_2_FS/pipe_step_2_scripts/SymmetricalUncert_Fselection.py
scp ./scripts/Relief_Fselection.py ./pipe_step_2_FS/pipe_step_2_scripts/Relief_Fselection.py
scp ./scripts/InformationGainRatio_Fselection.py ./pipe_step_2_FS/pipe_step_2_scripts/InformationGainRatio_Fselection.py
scp ./scripts/Inforgain_Fselection.py ./pipe_step_2_FS/pipe_step_2_scripts/Inforgain_Fselection.py

scp ./scripts/ensemble_weighting.py ./pipe_step_3_FAggregation/pipe_step_3_make_ensemble/ensemble_weighting.py

scp ./scripts/create_venn.py ./pipe_step_3_FAggregation/pipe_step_3_make_venn/create_venn.py
scp ./scripts/fileAggregate.py ./pipe_step_3_FAggregation/pipe_step_3_make_venn/fileAggregate.py

scp ./scripts/CreateAUC_DF.py ./pipe_step_3_FAggregation/pipe_step_3_make_aggregates/CreateAUC_DF.py
scp ./scripts/NB_SVM_functions.py ./pipe_step_3_FAggregation/pipe_step_3_make_aggregates/NB_SVM_functions.py

scp ./scripts/RandomForest_classifier_allfiles.py ./pipe_step_4_clf/pipe_step_4_clf_clfers/RF/RandomForest_classifier_allfiles.py
scp ./scripts/SVM_StratKfold3_gammaSuto_rbf.py ./pipe_step_4_clf/pipe_step_4_clf_clfers/SVM/SVM_StratKfold3_gammaSuto_rbf.py
scp ./scripts/preprocess_class_labels_for_classifiers.py ./pipe_step_4_clf/pipe_step_4_clf_clfers/preprocess_script/preprocess_class_labels_for_classifiers.py
scp ./scripts/NaiveBayes.py ./pipe_step_4_clf/pipe_step_4_clf_clfers/NB/NaiveBayes.py


scp ./scripts/Bar_Plot.py ./pipe_step_4_clf/result_auc_for_each_position/Bar_Plot.py


scp ./scripts/*sh .


# Make all bash scripts executable
for f in *.sh;do chmod +x $f;done
