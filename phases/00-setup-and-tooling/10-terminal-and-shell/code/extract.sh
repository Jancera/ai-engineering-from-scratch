grep "loss" fake_train.log | awk '{print $NF}' > losses.txt
