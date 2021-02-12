'''# Check for GPU and CPU consumption

import GPUtil
GPUtil.showUtilization()'''

import wandb

wandb login #a714d91fb701d5a1bbb4b2539a4d2b89c504ff5c
python tutorial.py


'''import tensorflow as tf
import wandb

wandb.init(config=tf.FLAGS)
estimator.train(hooks=[wandb.tensorflow.WandbHook(steps_per_log=1000)])

print("weights and biases done")'''