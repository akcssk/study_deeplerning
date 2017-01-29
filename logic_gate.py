import numpy as np
def perceptron (x1, x2, w1, w2, bias):
#2017/01/29
#パーセプトロンを利用したNAND回路
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
def NAND (x1, x2):
    return perceptron(x1, x2, w1=-0.5, w2=-0.5, bias=0.7)
def AND (x1, x2):
    #NAND回路だけで実装
    return NAND(NAND(x1, x2),NAND(x1, x2))
    #return perceptron(x1, x2, w1=0.5, w2=0.5, bias=-0.7)
def NOT (x1):
    #NANDの両端に同じ入力をする
    return NAND(x1 = x1, x2 = x1)
def OR (x1, x2):
    #NOTとNANDだけで実装
    return NAND(NOT(x1),NOT(x2))
    #return perceptron(x1, x2, w1=0.5, w2=0.5, bias=-0.3)
def XOR (x1, x2):
    #思いついたので作るただ、引き算は反則だ
    #return OR(x1, x2) - AND(x1, x2)
    #回路的に正しいのはこっち、
    return AND(NAND(x1, x2), OR(x1, x2))

print('-------AND--------')
assert(AND(0,0)) is 0
assert(AND(0,1)) is 0
assert(AND(1,0)) is 0
assert(AND(1,1)) is 1
print('-------NAND--------')
assert(NAND(0,0)) is 1
assert(NAND(0,1)) is 1
assert(NAND(1,0)) is 1
assert(NAND(1,1)) is 0
print('-------NOT--------')
assert(NOT(0)) is 1
assert(NOT(1)) is 0
print('-------OR--------')
assert(OR(0,0)) is 0
assert(OR(0,1)) is 1
assert(OR(1,0)) is 1
assert(OR(1,1)) is 1
print('-------XOR--------')
assert(XOR(0,0)) is 0
assert(XOR(0,1)) is 1
assert(XOR(1,0)) is 1
assert(XOR(1,1)) is 0
