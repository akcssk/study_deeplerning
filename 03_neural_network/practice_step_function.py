import numpy as np
import matplotlib.pyplot as plt

def step_function(np_xs):
#numpy配列を引数にとるステップ関数
    ys = np_xs > 0
    #print (repr(ys))
    return ys.astype(np.int)

#isはオブジェクトが同じかどうかを判定する.配列の中身を比較するときは使わない
#あと、numpy配列の比較は.all() .any()を使うらしい
assert(step_function(np.array([-1.0, 1.0, 2.0])) == [0, 1, 1]).all()

#ステップ関数のグラフ
x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y 軸の範囲を指定
plt.show()
