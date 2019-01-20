import numpy as np
import tensorflow as tf


feature_columns =[tf.feature_column.numeric_column("x",shape=[1])]

estimator = tf.estimator.LinearRegressor(feature_columns)

x_train = np.array([1.,2.,3.,6.,8.])
y_train = np.array([4.8,8.5,10.4,21.0,25.3])

x_eval = np.array([2.,5.,7.,9.])
y_eval = np.array([7.6,17.2,23.6,28.8])

train_input_fn = tf.estimator.inputs.numpy_input_fn({"x":x_train},y_train,batch_size=2,num_epochs=None,shuffle=True)

train_input_fn2 = tf.estimator.inputs.numpy_input_fn({"x":x_train},y_train,batch_size=2,num_epochs=1000,shuffle=False)

evalu_input_fn = tf.estimator.inputs.numpy_input_fn({"x":x_eval},y_eval,batch_size=2,num_epochs=1000,shuffle=False)

estimator.train(input_fn=train_input_fn,steps=1000)

train_metrics = estimator.evaluate(input_fn=train_input_fn2)
print("train metrics:%r"%train_metrics)

eval_metrics = estimator.evaluate(input_fn=evalu_input_fn)
print("eval metrics:%s"%eval_metrics)
