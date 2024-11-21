import numpy as np
from Lagrange import Lagrange
from Newton import Newton
from CubicSplineFree import CubicSplineFree
#通过上述自建库调用

"待插值的原始数据"
AXY_1 = np.array([[2005, 72.8], [2010, 74.2], [2015, 75.2], [2020, 76.4]])
NT = Newton(AXY_1)
"计算x=2000,2013,2018,2025的近似值"
x0 = np.array([2000, 2013, 2018, 2025])
y0 = np.array([])
for x in x0:
    y0 = np.append(y0, NT.num(x))
print("地区1的牛顿插值=", y0)
"生成图像"
NT.visualize(2000, 2030, 1000, True)
"生成差值表"
Table = NT.f()[1]
print(Table)


"拉格朗日插值部分"
AXY_2 = np.array([[2005, 70.2], [2010, 70.2], [2015, 70.3], [2020, 71.2]])
LA = Lagrange(AXY_2)
Num_LA = np.array([])
"复用题设预测年份x0"
for x in x0:
    Num_LA = np.append(Num_LA, LA.num(x))
print("地区2的拉格朗日=", Num_LA)
LA.visualize(2000, 2030, 1000, True)

"Q1.3,三次样条插值"

# district_1
CSF_1 = CubicSplineFree(AXY_1)
Num_CSF_1 = np.array([])
for x in x0:
    Num_CSF_1 = np.append(Num_CSF_1, CSF_1.num(x))
print("地区1三次样条=",Num_CSF_1)
CSF_1.visualize(2000, 2030, 100, True)

# district_2
CSF_2 = CubicSplineFree(AXY_2)
Num_CSF_2 = np.array([])
for x in x0:
    Num_CSF_2 = np.append(Num_CSF_2, CSF_2.num(x))
print("地区2三次样条=", Num_CSF_2)
CSF_1.visualize(2000, 2030, 100, True)



