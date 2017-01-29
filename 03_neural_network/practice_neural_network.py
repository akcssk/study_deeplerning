from practice_sigmoid_function import sigmoid
import numpy as np

def identity_function(x):
#回帰問題の場合、出力層で使う恒等関数
    return x

#入力
X = np.array([1.0, 0.5])
#1層目
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

# 1層目の重み付き和
print('---1層目入力---')
print(X)
print('--------------')
print(X.shape)
print(W1.shape)
print(B1.shape)
A1 = np.dot(X, W1) + B1
Z1 = sigmoid(A1)
print(A1)
print('---1層目出力=2層目入力---')
print(Z1)
print('--------------')
# 2層目
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

print(Z1.shape) # (3,)
print(W2.shape) # (3, 2)
print(B2.shape) # (2,)
A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)
print(A2)
print('---2層目出力=出力層入力---')
print(Z2)
print('--------------')

#出力層
W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])
A3 = np.dot(Z2, W3) + B3
Y = identity_function(A3) # もしくは Y = A3

print('---出力---')
print(Y)
print('--------------')
