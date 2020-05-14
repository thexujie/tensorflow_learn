import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']= '2'
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

print("build with cuda ? ", tf.test.is_built_with_cuda())
print("is gpu available ? ", tf.test.is_gpu_available(cuda_only=False,min_cuda_compute_capability=None))

v1 = tf.constant([1,2,3,4,5])
v2 = tf.constant([6,7,8,9,10])
v_add = tf.add(v1, v2)
with tf.Session() as ss:
    print(ss.run(v_add))

