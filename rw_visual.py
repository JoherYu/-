#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 在关闭窗口后，只要没输入'n'就再次生成图像
while True:
    rw = RandomWalk(50000)  # 创建随机漫步实例
    rw.fill_walk()
    
    # 绘制图像
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers, 
                cmap=plt.cm.Blues)
    plt.scatter(0, 0, s=100, c='green')
    plt.scatter(rw.x_values[-1], rw.y_values[-1], s=100, c='red')
    plt.axes().get_xaxis().set_visible(False)  # 隐藏坐标轴
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()
    
    keep_running= input("是否重新在走一次？输入任意键重新走一次，输入'n'退出: ")
    if keep_running == 'n':
        break