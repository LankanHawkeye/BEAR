echo ""
echo "Venn Diagram Creation and Feature Aggregation Started."
cd ./pipe_step_3_make_venn/
/usr/local/bin/python3.7 create_venn.py
cd ..
echo ""
echo "Venn Diagram Creation and Feature Aggregation Complete."
echo "=========================="

echo ""
echo "Feature Ensemble Creation Started."
cd ./pipe_step_3_make_ensemble/
/usr/local/bin/python3.7 ensemble_weighting.py
cd ..
echo ""
echo "Feature Ensemble Creation Complete."

echo ""
scp ./pipe_step_3_make_aggregates/*csv ../pipe_step_4_clf/pipe_step_4_clf_clfers/NB/
scp ./pipe_step_3_make_aggregates/*csv ../pipe_step_4_clf/pipe_step_4_clf_clfers/SVM/
scp ./pipe_step_3_make_aggregates/*csv ../pipe_step_4_clf/pipe_step_4_clf_clfers/RF/
scp ./pipe_step_3_make_ensemble/ensemble_output/Ensemble.csv ../pipe_step_4_clf/pipe_step_4_clf_clfers/NB/
scp ./pipe_step_3_make_ensemble/ensemble_output/Ensemble.csv ../pipe_step_4_clf/pipe_step_4_clf_clfers/SVM/
scp ./pipe_step_3_make_ensemble/ensemble_output/Ensemble.csv ../pipe_step_4_clf/pipe_step_4_clf_clfers/RF/
echo " "
echo "All Newly Created Feature Files were Assigned as Classifier Input Files"
