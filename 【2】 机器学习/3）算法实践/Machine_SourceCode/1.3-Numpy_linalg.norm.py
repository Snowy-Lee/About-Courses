import numpy as np
x = np.array([
    [0,3,4],
    [1,6,4]])

print("默认参数(矩阵整体元素平方和开根号，不保留矩阵二维特征)：",np.linalg.norm(x))
print("矩阵整体元素平方和开根号，保留矩阵二维特征：",np.linalg.norm(x,keepdims=True))

print("矩阵每个行向量求向量的2范数：",np.linalg.norm(x,axis = 1,keepdims=True))
print("矩阵每个列向量求向量的2范数：",np.linalg.norm(x,axis = 0,keepdims=True))

print('矩阵1范数：',np.linalg.norm(x,ord = 1,keepdims = True))
print('矩阵2范数：',np.linalg.norm(x,ord = 2,keepdims = True))
print('矩阵∞范数：',np.linalg.norm(x,ord = np.inf,keepdims = True))

print('矩阵每个行向量求向量的1范数：',np.linalg.norm(x,ord = 1,axis = 1,keepdims=True))