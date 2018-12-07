import json
import pygal
import math

# 读取数据
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)
    
# 储存每日信息
dates, months, weeks, weekdays, close = [], [], [], [], []
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

# 绘制图像
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价对数变换(￥)'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('log收盘价', close_log)

line_chart.render_to_file('收盘价对数变换折线图(￥).svg')

'''# 建立收盘数据仪表盘，需确定浏览器兼容性问题
with open('收盘价Dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write('\
        <html><head><title></title><metacharset="utf-8"></head><body>\n')
    for svg in ('收盘价折线图(￥).svg', '收盘价对数变换折线图(￥).svg'):
        html_file.write('   <object type="images/svg+xml" data="{0}"\
                        height=500></object>\n'.format(svg))
        html_file.write('</body></html>')'''