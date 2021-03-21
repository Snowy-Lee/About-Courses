import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#载入数据，必要的时候可以查看下数据的情况
source_url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'            
data = pd.read_csv(source_url,header=None,prefix='x')
data.columns = ['cluster','Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue','OD280/OD315 of diluted wines','Proline']

#print(data.info())
#print(data.head())
#print(data.tail())
#print(data.describe())

#由于data第一列为数据集分好的标签，先剔除。
x = data.iloc[:,1:].values
# print(x.shape)
y = data.iloc[:,0].values
from sklearn.ensemble import RandomForestClassifier
RFC = RandomForestClassifier(n_estimators=15000,n_jobs= -1 ,random_state=0)
RFC.fit(x,y)
#构造随机森林，拟合数据。

import_level = RFC.feature_importances_ #这个方法可以调取关于特征重要程度
x_columns = data.columns[1:]
index = np.argsort(import_level)[::-1]
for each in range(x.shape[1]):
    print('The important level of '+ x_columns[each]+ ':      '+ str(import_level[index[each]]))
#对于最后需要逆序，个人的理解是做了类似决策树回溯的取值。从叶子收敛到根，根部重要程度高于叶子。

#最后在可视化以下图
plt.figure(figsize=(10,6))
plt.title('红酒数据集中各个特征的重要程度',fontsize = 18)
plt.ylabel('import level',fontsize = 15,rotation = 90)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
for i in range(x_columns.shape[0]):
    plt.bar(i,import_level[index[i]],color = 'orange',align = 'center')
    plt.xticks(np.arange(x_columns.shape[0]),x_columns,rotation = 90,fontsize = 15)
