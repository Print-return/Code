import pandas as pd
print("运行速度较慢，请等待...")
print(">>>>>>  可能需要十秒钟，不要终止程序  >>>>>>")

#四阶龙格-库塔法
#求一阶常微分方程，相应的特解
#x变量的区间
a = 0
b = 90
#已知条件
X = [0]
Y = [0.001]
h = 0.00001   #设置步长
n = (b-a)/h    #步数
def f(x,y):
    df = 9.8/239.46*(239.46 - 1035.71 * 0.2058 - 0.62 * y)*1/y
    return df
#程序运行
for i in range(int(n)):
    x1 = X[i]+h
    X.append(x1)    #x1=x0+h
    k1 = f(X[i], Y[i])
    k2 = f(X[i]+h/2, Y[i]+h/2*k1)
    k3 = f(X[i]+h/2, Y[i]+h/2*k2)
    k4 = f(X[i]+h, Y[i]+h*k3)
    y1 = Y[i] + h/6*(k1+2*k2+2*k3+k4)
    Y.append(y1)


list = []
for i in range(len(X)):
    list.append([X[i],Y[i]])

dataframe = pd.DataFrame(list)
print("k\ts\tv")
print(dataframe)

# import numpy as np
# import matplotlib.pyplot as plt
#
# DT = np.array(input("份数：").split(' '))
# y0 = int(input("函数起点："))
#
# def f(y):
#     return np.exp(-y)
#
# def Runge_Kutta(t, y0):
#     n = len(t)
#     y = np.zeros(n)
#     y[0] = y0
#     for i in range(0, n-1):
#         h = t[i+1] - t[i]
#         k1 = f(y[i])
#         k2 = f(y[i] + h/2*k1)
#         k3 = f(y[i] + h/2*k2)
#         k4 = f(y[i] + h*k3)
#         y[i+1] = y[i] + h/6 * (k1 + 2*k2 + 2*k3 + k4)
#     return y
#
# for dt in DT:
#     dt = int(dt)
#     t = np.linspace(0, 10, dt)
#     y = Runge_Kutta(t, 0)
#     plt.plot(t, y)
#
# plt.show()