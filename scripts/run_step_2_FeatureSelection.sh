# Run the bash script for feature selection
echo ""
echo "Feature Selection Started."
echo " "
echo " "
/usr/local/bin/python3.7 ./pipe_step_2_FS/pipe_step_2_scripts/Correlation_Fselection.py ./pipe_step_2_FS/pipe_step_2_input/input.csv ./pipe_step_2_FS/pipe_step_2_output/
echo " "
/usr/local/bin/python3.7 ./pipe_step_2_FS/pipe_step_2_scripts/Inforgain_Fselection.py ./pipe_step_2_FS/pipe_step_2_input/input.csv ./pipe_step_2_FS/pipe_step_2_output/
echo " "
/usr/local/bin/python3.7 ./pipe_step_2_FS/pipe_step_2_scripts/InformationGainRatio_Fselection.py ./pipe_step_2_FS/pipe_step_2_input/input.csv ./pipe_step_2_FS/pipe_step_2_output/
echo " "
/usr/local/bin/python3.7 ./pipe_step_2_FS/pipe_step_2_scripts/Relief_Fselection.py ./pipe_step_2_FS/pipe_step_2_input/input.csv ./pipe_step_2_FS/pipe_step_2_output/
echo " "
/usr/local/bin/python3.7 ./pipe_step_2_FS/pipe_step_2_scripts/SymmetricalUncert_Fselection.py ./pipe_step_2_FS/pipe_step_2_input/input.csv ./pipe_step_2_FS/pipe_step_2_output/
echo " "
scp ./pipe_step_2_FS/pipe_step_2_output/*.csv ./pipe_step_4_clf/pipe_step_4_clf_clfers/NB
scp ./pipe_step_2_FS/pipe_step_2_output/*.csv ./pipe_step_4_clf/pipe_step_4_clf_clfers/SVM
scp ./pipe_step_2_FS/pipe_step_2_output/*.csv ./pipe_step_4_clf/pipe_step_4_clf_clfers/RF
scp ./pipe_step_2_FS/pipe_step_2_output/*.csv ./pipe_step_3_FAggregation/pipe_step_3_Fselected_input/

echo ""
echo ""
echo "================================================="
echo "Feature Selection is Complete"
echo ""
echo "Please, run the following bash script with numeric argument (top_features) now. "
echo ""
echo "bash ./run_step_3_vennDiFeAEns_without_bootstrapping.sh top_featuers"
