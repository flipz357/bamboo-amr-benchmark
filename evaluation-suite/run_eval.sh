metric=$1

python evaluate4tasks.py -path_sts_prediction_file_main sim-predictions/sts-$metric-main.txt \
    -path_sick_prediction_file_main sim-predictions/sick-$metric-main.txt \
    -path_para_prediction_file_main sim-predictions/para-$metric-main.txt \
    -path_sts_prediction_file_syno sim-predictions/sts-$metric-syno.txt \
    -path_sick_prediction_file_syno sim-predictions/sick-$metric-syno.txt \
    -path_para_prediction_file_syno sim-predictions/para-$metric-syno.txt \
    -path_sts_prediction_file_reify sim-predictions/sts-$metric-reify.txt \
    -path_sick_prediction_file_reify sim-predictions/sick-$metric-reify.txt \
    -path_para_prediction_file_reify sim-predictions/para-$metric-reify.txt \
    -path_sts_prediction_file_roleconf sim-predictions/sts-$metric-role_confusion.txt \
    -path_sick_prediction_file_roleconf sim-predictions/sick-$metric-role_confusion.txt \
    -path_para_prediction_file_roleconf sim-predictions/para-$metric-role_confusion.txt \
