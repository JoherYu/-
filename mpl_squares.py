#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

values = [1, 2, 3, 4, 5]
squares = [1, 4, 9,16, 25]

plt.plot(values, squares, linewidth=5)  # 生成图表

# 设置标题标签样式
plt.title("平方数", fontsize=24, fontproperties="SimHei")  # 设置中文字体后，字
                                                           # 体大小失效？
plt.xlabel("值", fontsize=14, fontproperties="SimHei")
plt.ylabel("值的平方", fontsize=14, fontproperties="SimHei")
plt.tick_params(axis='both', labelsize=14)  # 刻度大小设置

plt.show()  # 显示图表