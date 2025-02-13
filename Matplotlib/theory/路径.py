import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patheffects as path_effects
import matplotlib.patches as patches
import numpy as np
'''
#路径代码
#STOP:整个路径终点标记。MOVETO:提笔并移动到指定顶点。LINETO:从当前位置向指定顶点画线。
# CURVE3:从当前位置，以给定控制点向给定端点画贝塞尔曲线。CURVE4:从当前位置，以给定控制点向给定端点画三次贝塞尔曲线。
# CLOSEPOLY:向当前折线的起点画线。


#绘制（0，0）到（1，1）的单位矩阵
verts = [(0,0),(0,1),(1,1),(1,0),(0,0)]
codes = [Path.MOVETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.CLOSEPOLY,]
path = Path(verts,codes)
fig = plt.figure()
ax = fig.add_subplot(111)
patch = patches.PathPatch(path,facecolor='orange',lw=2)
ax.add_patch(patch)
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
plt.show()

#贝塞尔
vert_s = [(0,0),(0.2,1),(1,0.8),(0.8,0),]
codes = [Path.MOVETO,Path.CURVE4,Path.CURVE4,Path.CURVE4,]
path = Path(vert_s,codes)
fig = plt.figure()
ax = fig.add_subplot(111)
patch = patches.PathPatch(path,facecolor="none",lw = 2)
ax.add_patch(patch)
xs,ys = zip(*vert_s)
ax.plot(xs,ys,'x--',lw=2,color = 'k',ms=10)
ax.text(-0.05,-0.05,'P0')
ax.text(0.15,1.05,'P1')
ax.text(1.05,0.85,'P2')
ax.text(0.85,-0.05,'P3')
ax.set_xlim(-0.1,1.1)
ax.set_ylim(-0.1,1.1)
plt.show()

#复合路径
import matplotlib.path as path
fig = plt.figure()
ax = fig.add_subplot(111)
np.random.seed(19680801)
data = np.random.randn(1000)
n,bins = np.histogram(data,100)
left = np.array(bins[:-1])
right = np.array(bins[1:])
bottom = np.zeros(len(left))
top = bottom+n
n_rect_s = len(left)
n_vert_s = n_rect_s*(1+3+1)
vert_s = np.zeros((n_vert_s,2))
codes = np.ones(n_vert_s,int)* path.Path.LINETO
codes[::5] = path.Path.MOVETO
codes[4::5] = path.Path.CLOSEPOLY
vert_s[0::5,0] = left
vert_s[0::5,1] = bottom
vert_s[1::5,0] = left
vert_s[1::5,1] = top
vert_s[2::5,0] = right
vert_s[2::5,1] = top
vert_s[3::5,0] = right
vert_s[3::5,1] = bottom
bar_path = path.Path(vert_s,codes)
patch = patches.PathPatch(bar_path,facecolor='g',edgecolor='y',alpha = 0.5)
ax.add_patch(patch)
ax.set_xlim(left[0],right[-1])
ax.set_ylim(bottom.min() ,top.max())
plt.show()

#路径效果
fig = plt.figure(figsize=(5,1.5))
text_val = fig.text(0.5,0.5,'Hello path effects world!\nThis is the normal path effect.\nPretty dull,huh?',
                    ha='center',va='center',size=20)
text_val.set_path_effects([path_effects.Normal()])
plt.show()

#添加阴影
text = plt.text(0.5,0.5,'Hello path effects world!',
                path_effects = [path_effects.withSimplePatchShadow()])
plt.plot([0,3,2,5],linewidth=5,color='b',path_effects=[path_effects.SimpleLineShadow(),path_effects.Normal()])
plt.show()

#以粗体绘制轮廓
fig = plt.figure(figsize=(7,1))
text_val = fig.text(0.5,0.5,'This text stands out because of\nits black border.',color='white',
                    ha='center',va='center',size = 30)
text_val.set_path_effects([path_effects.Stroke(linewidth=3,foreground='black'),
                           path_effects.Normal()])
plt.show()
'''
#黑体阴影
fig = plt.figure(figsize=(8,1))
text_val = fig.text(0.02,0.5,'Hatch shadow',fontsize = 75,weight=1000,va = 'center')
text_val.set_path_effects([path_effects.PathPatchEffect(offset=(4,-4),hatch='xxxx',facecolor = 'gray'),
                           path_effects.PathPatchEffect(edgecolor='w',linewidth=1.1,facecolor = 'k')])
plt.show()