# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 15:04:05 2023

@author: 86319
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 样本数据
x = np.array([0, 1, 2, 3, 4, 5, 6, 7])
y = np.array([7.82, 7.93, 7.98, 7.99, 7.92, 7.91, 7.80, 7.71])

# 定义二次函数模型
def quadratic_func(x, a, b, c):
    return a*x**2 + b*x + c

# 利用curve_fit函数拟合数据
popt, pcov = curve_fit(quadratic_func, x, y)

# 输出拟合参数
print("二次函数拟合参数：a={:.4f}, b={:.4f}, c={:.4f}".format(*popt))

# 输出二次函数拟合方程
print("二次函数拟合方程：y={:.4f}x^2+{:.4f}x+{:.4f}".format(*popt))

# 绘制数据点和拟合曲线
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.scatter(x, y, label='数据点')
plt.plot(x, quadratic_func(x, *popt), 'r-', label='拟合曲线')
plt.legend()

# 设置图形标题和坐标轴标签
plt.title('拟合结果')
plt.xlabel('x')
plt.ylabel('y')

# 显示图形
plt.show()
