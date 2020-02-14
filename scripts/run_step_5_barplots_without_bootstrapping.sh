echo "This step can only be run if previous step (run_step_4_clfEvaluation_without_bootstrapping.sh) completed successfully"
echo "This step uses the data files generated from the previous step"

# Generating Bar charts

cd ./pipe_step_4_clf/result_auc_for_each_position/
/usr/local/bin/python3.7 Bar_Plot.py
#/usr/local/bin/python3.7 Bar_Plot.py RF_AUC.txt
#/usr/local/bin/python3.7 Bar_Plot.py SVM_AUC.txt
cd ../..

echo ""
echo "Bar Plots Generated"
