CURR=$(pwd)
echo $CURR

for dat in sts sick para
do
    for task in reify main role_confusion syno
    do
    python simple_metric.py ../$dat/$task/tgt.test.amr ../$dat/$task/src.test.amr > sim-predictions/$dat-simpleMetric-$task.txt 
    done
done

