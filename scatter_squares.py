#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s=90, c=y_values, cmap=plt.cm.Blues)

# 设置标题、标签、坐标轴样式
plt.title("平方数", fontsize=24, fontproperties="SimHei")
plt.xlabel("值", fontsize=14, fontproperties="SimHei")
plt.ylabel("值的平方", fontsize=14, fontproperties="SimHei")
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000])

plt.show()
"""plt.savefig('squares_plot.png', bbox_inches='tight')  # 保存图表到本地 """