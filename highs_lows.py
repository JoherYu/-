#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

from matplotlib import pyplot as plt
from datetime import datetime

filename = "death_valley_2014.csv"

# 读取文件并获取最高气温、最低气温及日期
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    highs, lows, dates = [], [], []
    for row in reader:
        try:
            high = int(row[1])
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            low = int(row[3])
        except ValueError:
            print(current_date, '数据丢失')
        else:
            lows.append(low)
            highs.append(high)
            dates.append(current_date)
            
# 绘制折线图
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=1)

# 设置折线图样式
plt.title("加州死亡谷2014年每日最高、低气温", fontsize=24, 
                                              fontproperties="SimHei")
plt.xlabel("", fontsize=16, fontproperties="SimHei")
plt.ylabel("温度(F)", fontsize=16, fontproperties="SimHei")
plt.tick_params(axis='both', which='major', labelsize=16)  
fig.autofmt_xdate()

plt.show()