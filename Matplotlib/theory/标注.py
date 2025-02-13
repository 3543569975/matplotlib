import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

'''
#基本标注
# arrowprops():width:箭头宽度。frac：箭头头部所占比例。
# headwidth:箭头底部的宽度，以点为单位。shrink:移动提示，并使其与注释点和文本存在一定的距离。
fig = plt.figure()
ax = fig.add_subplot(111)
t = np.arange(0,5,0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t,s,lw=2)
ax.annotate('local max',xy=(2,1),xytext=(3,1.5),arrowprops=dict(facecolor='k',shrink=0.05),)
ax.set_ylim(-2,2)
plt.show()

#使用框和文本标注
fig = plt.figure(1,figsize=(5,5))
fig.clf()
ax = fig.add_subplot(111)
ax.set_aspect(1)
x1 = -1 + np.random.randn(100)
y1 = -1 + np.random.randn(100)
x2 = -1 + np.random.randn(100)
y2 = -1 + np.random.randn(100)
ax.scatter(x1,y1,color='r')
ax.scatter(x2,y2,color='g')
bbox_props = dict(boxstyle='round',fc='w',ec='0.5',alpha = 0.9)
ax.text(-2,-2,'Sample A',ha='center',va='center',size=20,bbox = bbox_props)
ax.text(2,2,'Sample B',ha='center',va='center',size=20,bbox = bbox_props)
bbox_props = dict(boxstyle='rarrow',fc=(0.8,0.9,0.9),ec = 'b',lw=2)
t = ax.text(0,0,'Direction',ha='center',va='center',rotation=45,size=15,bbox = bbox_props)
bb = t.get_bbox_patch()
bb.set_boxstyle('rarrow',pad=0.6)
ax.set_xlim(-4,4)
ax.set_ylim(-4,4)
plt.draw()
plt.show()

#使用箭头标注
x1,y1 = 0.3,0.3
x2,y2 = 0.7,0.7
fig = plt.figure(1,figsize=(8,3))
fig.clf()
from mpl_toolkits.axes_grid1 import AxesGrid
from matplotlib.offsetbox import AnchoredText

def add_at(ax,t,loc=2):
    fp = dict(size=10)
    _at = AnchoredText(t,loc = loc,prop=fp)
    ax.add_artist(_at)
    return _at
grid = AxesGrid(fig,111,(1,4),label_mode='1',share_all=True)
grid[0].set_autoscale_on(False)
ax = grid[0]
ax.plot([x1,x2],[y1,y2],'.')
el = mpatches.Ellipse((x1,y1),0.3,0.4,angle=30,alpha=0.2)
ax.add_artist(el)
ax.annotate('',xy=(x1,y1),xycoords='data',xytext=(x2,y2),textcoords = 'data',
            arrowprops=dict(arrowstyle='-',color='0.5',patchB=None,shrinkB=0,connectionstyle='arc3,rad=0.3',
                            ),)
add_at(ax,'connect',loc=2)
ax = grid[1]
ax.plot([x1,x2],[y1,y2],'.')
el = mpatches.Ellipse((x1,y1),0.3,0.4,angle=30,alpha=0.2)
ax.add_artist(el)
ax.annotate('',xy=(x1,y1),xycoords='data',xytext=(x2,y2),textcoords='data',
            arrowprops=dict(arrowstyle='-',color='0.5',patchB=el,shrinkB=0,connectionstyle='arc3,rad=0.3',
                            ),)
add_at(ax,'clip',loc=2)
ax = grid[2]
ax.plot([x1,x2],[y1,y2],'.')
el = mpatches.Ellipse((x1,y1),0.3,0.4,angle=30,alpha=0.2)
ax.add_artist(el)
ax.annotate('',xy=(x1,y1),xycoords='data',xytext=(x2,y2),textcoords='data',
            arrowprops=dict(arrowstyle='-',color='0.5',patchB=el,shrinkB=5,connectionstyle='arc3,rad=0.3',
                            ),)
add_at(ax,'shrink',loc=2)
ax = grid[3]
ax.plot([x1,x2],[y1,y2],'.')
el = mpatches.Ellipse((x1,y1),0.3,0.4,angle=30,alpha=0.2)
ax.add_artist(el)
ax.annotate('',xy=(x1,y1),xycoords='data',xytext=(x2,y2),textcoords='data',
            arrowprops=dict(arrowstyle='fancy',color='0.5',patchB=el,shrinkB=5,connectionstyle='arc3,rad=0.3',
                            ),)
add_at(ax,'mutate',loc=2)
grid[0].set_xlim(0,1)
grid[0].set_ylim(0,1)
grid[0].axis['bottom'].toggle(ticklabels=False)
grid[0].axis['left'].toggle(ticklabels=False)
fig.subplots_adjust(left=0.05,right=0.95,bottom=0.05,top=0.95)
plt.draw()
plt.show()
'''
#数学表达式
t = np.arange(0,5,0.01)
plt.plot(t)
plt.title(r'mathematical',fontsize=20)
#制作下标和上标
plt.text(10,4,r'$\alpha_i > \beta_i$',fontsize = 20)
#编写0到无穷的x
plt.text(120,4,r'$\sum_{i=0}^ \infty x_i$',fontsize = 20)
#创建分数
plt.text(220,4,r'$\frac{3}{4} \binom{3}{4} \stackrel{3}{4}$',fontsize=20)
#创建二项式
plt.text(320,4,r'$\frac{5 - \frac{1}{x}}{4}$',fontsize=20)
#创建堆叠数字
plt.text(110,0.5,r'$(\frac{5 - \frac{1}{x}}{4})$',fontsize=20)
#创建堆叠数字
plt.text(220,0.5,r'$\left(\frac{5 - \frac{1}{x}}{4}\right)$',fontsize=20)
#创建根式
plt.text(350,0.5,r'$\sqrt{2}$',fontsize=20)
#创建根式
plt.text(440,0.5,r'$\sqrt[3]{x}$',fontsize=20)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

plt.title('mathematical',fontsize=20)
#字体编写
plt.text(0.3,0.8,r'$s(t) = \mathcal{A}\mathrm{sin}(2 \omega t)$',fontsize=20)
#字体编写
plt.text(0.3,0.5,r'$s(t) = \mathcal{A}\/\sin(2 \omega t)$',fontsize=20)
#创建重音符号
plt.text(0.4,0.2,r'$\hat i\ \ \hat \imath$',fontsize = 20)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

t = np.arange(0,2,0.01)
s = np.sin(2*np.pi*t)
plt.plot(t,s)
plt.title(r'$\alpha_i > \beta_i$',fontsize=20)
plt.text(1.1,-0.6,r'$\sum_{i=0}^\infty x_i$',fontsize=20)
plt.text(0.45,0.6,r'$\mathcal{A}\mathrm{sin}(2 \omega t)$',fontsize=20)
plt.xlabel('time (s)')
plt.ylabel('volts (mv)')
plt.show()