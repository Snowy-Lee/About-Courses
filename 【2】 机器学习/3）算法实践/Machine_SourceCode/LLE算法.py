from __future__ import division, print_function, absolute_import

import time
import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data/", one_hot=False)

# batch_size = 256
# n_input = 784  # MNIST data input (img shape: 28*28)

# total_batch = int(mnist.train.num_examples/batch_size)

print(mnist.train.images.shape, mnist.train.labels.shape)
# x_digits=minist.train.images
# estimator = PCA(n_components=2)
# x_pca = estimator.fit_transform(mnist.train.images)

from sklearn import manifold
start = time.clock()
# print(mnist.train.images[:10])

trans_data, err = manifold.locally_linear_embedding(X=mnist.train.images[:10000],n_neighbors=5,n_components=2)

elapsed = (time.clock() - start)
print("Time used:",elapsed)
# print(x_pca)
# print(x_pca[:,0])
# print(x_pca[:,1])

label=mnist.train.labels
# print(label)

# 显示图形，前两个参数为降维结果的两维，第三个是手写数字的标签
plt.scatter(trans_data[:, 0], trans_data[:, 1], c=mnist.train.labels[:10000])
# 以颜色显示三维图像的第三个维度
plt.colorbar()
plt.show()
