from sklearn.datasets.samples_generator import make_moons

X,y_true = make_moons(n_samples=1000,noise=0.15)

import matplotlib.pyplot as plt

plt.scatter(X[:,0],X[:,1],c=y_true)
plt.show()

import time

from sklearn.cluster import KMeans

t0 = time.time()
kmeans = KMeans(init = 'k-means++',n_clusters=2, random_state=8).fit(X)
t = time.time() - t0

plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_)
plt.title('time : %f'%t)
plt.show()

from sklearn.cluster import DBSCAN

t0 = time.time()
dbscan = DBSCAN(eps=.1,min_samples=6).fit(X)
t = time.time()-t0

plt.scatter(X[:, 0], X[:, 1], c=dbscan.labels_)
plt.title('time : %f'%t)
plt.show()

from sklearn.datasets.samples_generator import make_circles

X,y_true = make_circles(n_samples=2000,factor=0.45,noise=0.1)

plt.scatter(X[:,0],X[:,1],c=y_true)
plt.show()

t0 = time.time()
kmeans = KMeans(init = 'k-means++',n_clusters=2, random_state=8).fit(X)
t = time.time() - t0
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_)
plt.title('time : %f'%t)
plt.show()

t0 = time.time()
dbscan = DBSCAN(eps=.1,min_samples=6).fit(X)
t = time.time()-t0
plt.scatter(X[:, 0], X[:, 1], c=dbscan.labels_)
plt.title('time : %f'%t)
plt.show()