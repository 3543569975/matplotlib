import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.ticker as ticker


#轴容器
fig = plt.figure()
rect = fig.patch
rect.set_facecolor('lightgoldenrodyellow')
ax1 = fig.add_axes([0.1,0.3,0.4,0.4])
rect = ax1.patch
rect.set_facecolor('lightslategray')
for label in ax1.xaxis.get_ticklabels():
    label.set_color('red')
    label.set_rotation(90)#横轴字体倾斜角度
    label.set_fontsize(6)

for line in ax1.yaxis.get_ticklines():
    line.set_color('green')
    line.set_markersize(25)
    line.set_markeredgewidth(3)
plt.show()
#( 1)设置主副刻度格式
t = np.arange(0.0,100.0,1)
s = np.sin(0.1*np.pi*t)*np.exp(-t*0.01)
ax = plt.subplot(111)
#注意:一般都在ax中设置,不再plot中设置
plt.plot(t,s,'--r*')
#修改主刻度
xmajorLocator = MultipleLocator(20)
#将x主刻度标签设置为20的倍数
xmajorFormatter = FormatStrFormatter('%5.1f')
#设置x轴标签文本的格式
ymajorLocator = MultipleLocator(0.5)
#将y轴主刻度标签设置为0.5的倍数
ymajorFormatter = FormatStrFormatter('%1.1f')
#设置y轴标签文本的格式#设置主刻度标签的位置,标签文本的格式
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)
ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)
plt.show()

#刻度容器
np.random.seed(19680801)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(100*np.random.rand(20))
formatter = ticker.FormatStrFormatter('$%1.2f')
ax.yaxis.set_major_formatter(formatter)
for tick in ax.yaxis.get_major_ticks():
    tick.label10n = False
    tick.label20n = True
    tick.label2.set_color('green')
plt.show()