import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
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
# plt.show()

a = np.log(2)
print(a)