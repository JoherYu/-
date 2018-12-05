#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygal

from die import Die

# 创建两枚不同的投资
die_1 = Die()
die_2 = Die(10)

# 掷骰子并储存结果
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
# 计数每面结果出现多少次
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
hist = pygal.Bar()

# 绘制图像
hist.title = "同时掷六面骰和十面骰各50000次的结果"
hist.x_title = "结果"
hist.y_title = "频率"
hist.x_labels = list(range(2, 17))
hist.add('D6 + D10', frequencies)

hist.render_to_file('die_visual.svg')

