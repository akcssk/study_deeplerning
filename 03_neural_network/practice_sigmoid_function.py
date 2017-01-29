import numpy as np
import matplotlib.pyplot as plt

def sigmoid(xs):
#numpy配列を引数にとるシグモイド関数
#余談だけどスカラー値というのは大きさのみをもつ値。
#プログラミングでは、配列とかじゃないただの値
    return 1 / (1 + np.exp(-xs))

def step_function(np_xs):
#numpy配列を引数にとるステップ関数
    ys = np_xs > 0
    #print (repr(ys))
    return ys.astype(np.int)

def relu(xs):
    return np.maximum(0, xs)


#シグモイド関数のグラフ(stepとの比較。シグモイドの方がなめらか)
#arangeの中に-1.77635684e-14って値が出ているんだけど
# x = np.arange(-5.0, 5.0, 0.1)
# y1 = sigmoid(x)
# y2 = step_function(x)
# y3 = relu(x)
# #print(y)
# plt.plot(x, y1, label = 'sigmoid')
# plt.plot(x, y2, linestyle = '--', label = 'step')
# plt.plot(x, y3, linestyle = ':', label = 'relu')

# plt.ylim(-1, 3) # y 軸の範囲を指定
# plt.show()
