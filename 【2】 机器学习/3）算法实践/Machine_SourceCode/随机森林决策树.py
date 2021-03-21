from sklearn import datasets
digits = datasets.load_digits();

X = digits.data #特征矩阵
y = digits.target #标签矩阵
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3., random_state=8) #分割训练集和测试集
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
estimators = {}

# criterion: 分支的标准(gini/entropy)
estimators['tree'] = tree.DecisionTreeClassifier(criterion='gini',random_state=8) # 决策树

# n_estimators: 树的数量
# bootstrap: 是否随机有放回
# n_jobs: 可并行运行的数量
estimators['forest'] = RandomForestClassifier(n_estimators=20,criterion='gini',bootstrap=True,n_jobs=2,random_state=8) # 随机森林
from sklearn.model_selection import cross_val_score
import datetime

for k in estimators.keys():
    start_time = datetime.datetime.now()
    print('----%s----',k)
    estimators[k] = estimators[k].fit(X_train, y_train)
    pred = estimators[k].predict(X_test)
    print(pred[:10])
    print("%s Score: %0.2f" % (k, estimators[k].score(X_test, y_test)))
    scores = cross_val_score(estimators[k], X_train, y_train,scoring='accuracy' ,cv=10)
    print("%s Cross Avg. Score: %0.2f (+/- %0.2f)" % (k, scores.mean(), scores.std() * 2))
    end_time = datetime.datetime.now()
    time_spend = end_time - start_time
    print("%s Time: %0.2f" % (k, time_spend.total_seconds()))