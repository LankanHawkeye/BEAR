echo "This script takes a number as its first argument. This number represents the top features selected by ranking methods."
echo "Top feature number should be less than or equal to the total number of features"

# Access the folder with step 3
cd ./pipe_step_3_FAggregation/pipe_step_3_make_venn/

echo ""
echo "Venn Diagram Creation and Feature Aggregation Started."
/usr/local/bin/python3.7 create_venn.py $1
cd ../..
echo ""
echo "Venn Diagram Creation and Feature Aggregation Complete."
echo "=========================="

echo ""
echo "Feature Ensemble Creation Started."
cd ./pipe_step_3_FAggregation/pipe_step_3_make_ensemble/
/usr/local/bin/python3.7 ensemble_weighting.py
cd ../
echo ""
echo "Feature Ensemble Creation Complete."

echo ""
scp ./pipe_step_3_make_aggregates/*csv ../pipe_step_4_clf/pipe_step_4_clf_clfers/NB/
scp ./pipe_step_3_make_aggregates/*csv ../pipe_step_4_clf/pipe_step_4_clf_clfers/SVM/
scp ./pipe_step_3_make_aggregates/*csv ../pipe_step_4_clf/pipe_step_4_clf_clfers/RF/
scp ./pipe_step_3_make_ensemble/ensemble_output/Ensemble.csv ../pipe_step_4_clf/pipe_step_4_clf_clfers/NB/
scp ./pipe_step_3_make_ensemble/ensemble_output/Ensemble.csv ../pipe_step_4_clf/pipe_step_4_clf_clfers/SVM/
scp ./pipe_step_3_make_ensemble/ensemble_output/Ensemble.csv ../pipe_step_4_clf/pipe_step_4_clf_clfers/RF/
echo "================================================"
echo " "
echo "step complete."
echo "All Newly Created Feature Files were Assigned as Classifier Input Files"

echo ""
echo "Please, run the following bash script now. "

echo "bash ./bash run_step_4_clfEvaluation_without_bootstrapping.sh"
