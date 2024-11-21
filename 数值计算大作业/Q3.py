import Romberg_origin as R_o
import numpy as np


# 滚珠轴承：载荷计算
def f(x):
    return np.cos(x) * (1 - ((1 - np.cos(x)) / (2 * 0.6))) ** 1.1
Tn_list = R_o.compute_Tn(f, x_min=-np.arccos(1 - 0.6 * 2), x_max=np.arccos(1 - 0.6 * 2), epoch=24)
print("--------------------------------------  Situation: >>> Ball_Bearing<<  --------------------------------------")
print("Trapezoidal", Tn_list)
Sn_list = R_o.compute_Sn(Tn_list)
print("Simpson", Sn_list)
Cn_list = R_o.compute_Cn(Sn_list=Sn_list)
print("Cotes", Cn_list)
Rn_list = R_o.compute_Rn(Cn_list=Cn_list)
print("Romberg", Rn_list)
print("-------------------------------------------------------------------------------------------------------------")
print("\n \n \n")


# 滚柱轴承：载荷计算
def g(x):
    return np.cos(x) * (1 - ((1 - np.cos(x)) / (2 * 0.6))) ** 1.5
Tn_list = R_o.compute_Tn(g, x_min=-np.arccos(1 - 0.6 * 2), x_max=np.arccos(1 - 0.6 * 2), epoch=24)
print("--------------------------------------  Situation: >>> Roller_Bearing<<  --------------------------------------")
print("Trapezoidal:", Tn_list)
Sn_list = R_o.compute_Sn(Tn_list)
print("Simpson:", Sn_list)
Cn_list = R_o.compute_Cn(Sn_list=Sn_list)
print("Cotes:", Cn_list)
Rn_list = R_o.compute_Rn(Cn_list=Cn_list)
print("Romberg:", Rn_list)
print("-------------------------------------------------------------------------------------------------------------")
# import numpy as np
# from matplotlib import pyplot as plt
#
# x = np.linspace(0,6,1000)
# y = np.cos(2*np.pi*x)*np.exp(-x)+1.2
#
# plt.axis([np.min(x),np.max(x),0,np.max(y)])           #坐标范围
# plt.plot(x,y,label="$cos(2πx)e^{-x}+1.2$")            #画曲线，带图示
# plt.fill_between(x,y1=y,y2=0,where=(x>=0.7)&(x<=4),   #填充积分区域
#                  facecolor='blue',alpha=0.2)
# plt.text(0.5*(0.7+4),0.4,r"$\int_{0.7}^4(cos(2πx)e^{-x}+1.2)\mathrm{d}x$",
#          horizontalalignment='center',fontsize=14)    #增加说明文本
# plt.legend()                                          #显示图示
# plt.show()

print(1.613641465564148/(2*np.pi))
print(1.5179558745817645/(2*np.pi))

