import numpy as np
def perceptron (x1, x2, w1, w2, bias):
#2017/01/29
#パーセプトロンはXORを出せない。直線を引いて分断するだけなので
#非線形の分類でないと無理
#ここで多層パーセプトロンですよ
    x = np.array([x1, x2])
    w = np.array([w1, w2])
    tmp = np.sum(w*x) + bias
    if tmp <= 0:
        return 0
    else:
        return 1
def AND (x1, x2):
    return perceptron(x1, x2, w1=0.5, w2=0.5, bias=-0.7)
def NAND (x1, x2):
    return perceptron(x1, x2, w1=-0.5, w2=-0.5, bias=0.7)
def OR (x1, x2):
    return perceptron(x1, x2, w1=0.5, w2=0.5, bias=-0.3)
def XOR (x1, x2):
    #思いついたので作るただ、引き算は反則だ
    #return OR(x1, x2) - AND(x1, x2)
    #回路的に正しいのはこっち、
    return AND(NAND(x1, x2), OR(x1, x2))

print('-------AND--------')
print(AND(0,0))
print(AND(0,1))
print(AND(1,0))
print(AND(1,1))
print('-------NAND--------')
print(NAND(0,0))
print(NAND(0,1))
print(NAND(1,0))
print(NAND(1,1))
print('-------OR--------')
print(OR(0,0))
print(OR(0,1))
print(OR(1,0))
print(OR(1,1))
print('-------XOR--------')
print(XOR(0,0))
print(XOR(0,1))
print(XOR(1,0))
print(XOR(1,1))
