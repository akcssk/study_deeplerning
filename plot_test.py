import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1) # 0 から 6 まで 0.1 刻みで生成
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)


plt.plot(x, y1, label = 'sin')
plt.plot(x, y2, linestyle = '--', label = 'cos')
plt.plot(x, y3, linestyle = ':', label = 'cos')
# plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('sin & cos')#title
plt.legend()
plt.show()
