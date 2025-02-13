import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.transforms as transforms

'''
#数据变换
x = np.arange(0,10,0.005)
y = np.exp(-x/2.)*np.sin(2*np.pi*x)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y)
ax.set_xlim(0,10)
ax.set_ylim(-1,1)
plt.show()

#混合变换
fig = plt.figure()
ax = fig.add_subplot(111)
x = np.random.randn(1000)
ax.hist(x,30)
ax.set_title(r'$sigma=1 \/ \dots \/ \sigma=2$',fontsize=16)
trans = transforms.blended_transform_factory(ax.transData,ax.transAxes)
rect = patches.Rectangle((1,0),width=1,height=1,transform=trans,color='yellow',alpha=0.5)
ax.add_patch(rect)
plt.show()
'''
#创建阴影效果
fig = plt.figure()
ax = fig.add_subplot(111)
#正弦波
x = np.arange(0,2,0.01)
y = np.sin(2*np.pi*x)
line, = ax.plot(x,y,lw=3,color = 'blue')
#向下移动物体两个点
dx,dy = 2/72,-2/72
offest = transforms.ScaledTranslation(dx,dy,fig.dpi_scale_trans)
shadow_transfrom = ax.transData + offest
#现在用偏移变换绘制相同的数据，使用zorder确保线下
ax.plot(x,y,lw=3,color = 'gray',transform = shadow_transfrom,zorder=0.5*line.get_zorder())
#使用偏移变换创建阴影效果
ax.set_title('creating a shadow effect with an offset transform')
plt.show()