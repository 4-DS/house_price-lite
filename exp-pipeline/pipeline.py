import sys, os
sys.path.append('../')

import sinara.experiment as exp

data_load = exp.Experiment.function("data_load.ipynb")
data_prep = exp.Experiment.function("data_prep.ipynb")
model_train = exp.Experiment.function("model_train.ipynb")
model_eval = exp.Experiment.function("model_eval.ipynb")
model_test = exp.Experiment.function("model_test.ipynb")


r1 = f1()
r2 = f2(r1.x, r1.y)
f3()
