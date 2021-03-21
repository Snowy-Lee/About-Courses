# -*- coding: utf-8 -*-

from time import time
from PIL import Image
import glob
import numpy as np
import sys
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

# 设置解释器为utf8编码，不知为何文件开头的注释没用。
# 尽管这样设置，在IPython下仍然会出错，只能用原装Python解释器执行本程序
# reload(sys)
# sys.setdefaultencoding("utf8")
# print sys.getdefaultencoding()

PICTURE_PATH = u"C:\\Users\\zhangliang\\Desktop\\att_faces"

all_data_set = []  # 原始总数据集，二维矩阵n*m，n个样例，m个属性
all_data_label = []  # 总数据对应的类标签


def get_picture():
    label = 1
    # 读取所有图片并一维化
    while (label <= 20):
        for name in glob.glob(PICTURE_PATH + "\\s" + str(label) + "\\*.pgm"):
            img = Image.open(name)
            # img.getdata()
            # np.array(img).reshape(1, 92*112)
            all_data_set.append(list(img.getdata()))
            all_data_label.append(label)
        label += 1


get_picture()

n_components = 16 
pca = PCA(n_components=n_components, svd_solver='auto',
          whiten=True).fit(all_data_set)
# PCA降维后的总数据集
all_data_pca = pca.transform(all_data_set)
# X为降维后的数据，y是对应类标签
X = np.array(all_data_pca)
y = np.array(all_data_label)
n_estimators = [10,11,12,13,14,15,16,17,18,19,20]
criterion_test_names = ["gini", "entropy"]

# 输入核函数名称和参数gamma值，返回SVM训练十折交叉验证的准确率
def RandomForest(n_estimators,criterion):
    # 十折交叉验证计算出平均准确率
    # 交叉验证，随机取
    kf = KFold(n_splits=10, shuffle=True)
    precision_average = 0.0
    # param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5]}  # 自动穷举出最优的C参数
    # clf = GridSearchCV(SVC(kernel=kernel_name, class_weight='balanced', gamma=param),
    #                    param_grid)

    parameter_space = {
        "min_samples_leaf": [2, 4, 6],
    }
    clf = GridSearchCV(RandomForestClassifier(random_state=14,n_estimators = n_estimators,criterion = criterion), parameter_space, cv=5)
    for train, test in kf.split(X):
        clf = clf.fit(X[train], y[train])
        # print(clf.best_estimator_)
        test_pred = clf.predict(X[test])
        # print classification_report(y[test], test_pred)
        # 计算平均准确率
        precision = 0
        for i in range(0, len(y[test])):
            if (y[test][i] == test_pred[i]):
                precision = precision + 1
        precision_average = precision_average + float(precision) / len(y[test])
    precision_average = precision_average / 10
    # print (u"准确率为" + str(precision_average))
    return precision_average


#print("precision_average : ",RandomForest())

# t0 = time()
#kernel_to_test = ['rbf', 'poly', 'sigmoid']
# # rint SVM(kernel_to_test[0], 0.1)
# plt.figure(1)
#
for criterion in criterion_test_names:
    x_label = []
    y_label = []
    for i in n_estimators:
        y_label.append(RandomForest(i,criterion))
        x_label.append(i)
    plt.plot(x_label, y_label, label=criterion)

# print("done in %0.3fs" % (time() - t0))
plt.xlabel("criterion")
plt.ylabel("Precision")
plt.title('Different  Contrust')
plt.legend()
plt.show()


