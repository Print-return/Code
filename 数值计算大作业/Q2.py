import numpy as np
import matplotlib.pyplot as plt
from FitSquares import FitSquares_polynomial as Fp
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
              13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])
Y = np.array([14.4, 14.4, 14.4, 14.4, 13.9, 13.9, 13.9, 14.4, 15.6, 17.8, 19.4, 20.0,
              18.9, 18.9, 18.3, 17.8, 17.2, 17.2, 16.7, 16.7, 15.6, 15.6, 15.0, 14.4])
Arr = np.c_[X, Y]

# 线性拟合 1，x
FP_1 = Fp(Arr, 2)
print(FP_1.delta(), FP_1.an)
print("x=20处的值为=", FP_1.num(20))
FP_1.visualize(0, 24, 10000, True)


# 使用拟合基函数 1, x, x2 进行拟合
FP_2 = Fp(Arr, 3)
print(FP_2.delta(), FP_2.an)
print("x=20处的值为=", FP_2.num(20))
FP_2.visualize(0, 24, 10000, True)


"绘制全部曲线"
fig = plt.figure()
time = np.linspace(0, 25, 1000)
FP_1_num = np.array([])
FP_2_num = np.array([])

for x in time:
    FP_1_num = np.append(FP_1_num, FP_1.num(x))
    FP_2_num = np.append(FP_2_num, FP_2.num(x))
print(FP_1_num)
print(FP_2_num)
plt.plot(time,FP_1_num, label="Linear Fit", lw=1)
plt.plot(time,FP_2_num,label="Quadratic fitting", lw=1)
plt.plot(X, Y, label="Origin", lw=1)
plt.legend()
plt.show()



# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
#
# #使用linspace（）方法构成数据
# x = np.linspace(0, 2 * np.pi, 50)  #
# y1 = np.sin(x)
# y2 = np.cos(x)
# #转化数据形式
# df = pd.DataFrame([x,y1,y2]).T
# #对列重新命名
# df.columns = ['x','sin(x)','cos(x)']
# #数据写入图像，命名图例
# plt.plot(df['x'],df['sin(x)'],label='sin(x)')
# plt.plot(df['x'],df['cos(x)'],label='cos(x)')
# plt.legend()
#
