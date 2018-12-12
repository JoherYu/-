#!/usr/bin/env python3
# -*- coding: utf-8 -*-]

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 从GitHub API获取数据并从获取的数据中保存所有返回的仓库对象
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
response_dict = r.json()
repo_dicts = response_dict['items']

# 可视化
names, plot_dicts = [], []

for repo_dict in repo_dicts:
    
    names.append(repo_dict['name'])
    
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),  # str注意
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)
    
# 设置样式
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()

my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)

chart.title = '2018年12月12日GitHub上star最多的项目'
chart.x_labels = names
chart.add('', plot_dicts)

chart.render_to_file('python_repos.svg')