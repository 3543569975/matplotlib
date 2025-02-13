import matplotlib.pyplot as plt
import matplotlib.patches as m_patches
import matplotlib.lines as m_lines
from matplotlib.legend_handler import HandlerLine2D
from matplotlib.legend_handler import HandlerPatch
from numpy.random import randn

'''
#代理艺术家
black_patch = m_patches.Patch(color='black',label = 'The black data')
plt.legend(handles = [black_patch])
plt.show()
#带有标记的线条
blue_line = m_lines.Line2D([],[],color='blue',marker = '*',
                           markersize=15,label = 'Blue stars')
plt.legend(handles = [blue_line])
plt.show()

#图例位置
plt.subplot(211)
plt.plot([1,2,3],label = 'text1')
plt.plot([3,2,1],label = 'text2')
#将图例放到子图的上方，扩展自身来完全利用提供的边界框
plt.legend(bbox_to_anchor = (0.,1.02,1.,0.102),loc=3,ncol=2,mode='expand',borderaxespad=0.)
plt.subplot(223)
plt.plot([1,2,3],label='text1')
plt.plot([3,2,1],label='text2')
#将图例放到这个小型子图的右侧
plt.legend(bbox_to_anchor=(1.05,1),loc = 2,borderaxespad=0.)
plt.show()

#同轴域的多个图例
line1, = plt.plot([1,2,3],label='line1',linestyle='--')
line2, = plt.plot([3,2,1],label='line2',linewidth=4)
#为第一个线条创建图例
first_legend = plt.legend(handles=[line1],loc=1)
#手动将图例添加到当前轴域
ax = plt.gca().add_artist(first_legend)
#为第二个线条创建另一个图例
plt.legend(handles=[line2],loc=10)
plt.show()
'''
#图例处理器
line1, = plt.plot([1,2,3],label='line1',marker = 'o')
line2, = plt.plot([3,2,1],label='line2',marker = 'o')
plt.legend(handler_map = {line1:HandlerLine2D(numpoints=1)})
plt.show()
#将两个图例相互叠加
z = randn(10)
red_dot, = plt.plot(z,'ro',markersize = 15)
#将白色十字放置在一些数据上
white_cross, = plt.plot(z[:5],'w+',markeredgewidth=3,markersize=15)
plt.legend([red_dot,(red_dot,white_cross)],['Attr A','Attr A+B'])
plt.show()

#自定义图例处理器
class AnyObject(object):
    pass
class AnyObjectHandler(object):
    def legend_artist(self,legend,orig_handle,fontsize,handlebox):
        x0,y0 = handlebox.xdescent,handlebox.ydescent
        width,height = handlebox.width,handlebox.height
        patch = m_patches.Rectangle([x0,y0],width,height,facecolor='red',
                                    edgecolor='black',hatch='xx',lw = 3,
                                    transform = handlebox.get_transform())
        handlebox.add_artist(patch)
        return patch
plt.legend([AnyObject()],['My first handler'],
           handler_map={AnyObject:AnyObjectHandler()})
plt.show()

#自定义生成椭圆的图例键
class HandlerEllipse(HandlerPatch):
    def create_artist(self,legend,orig_handle,xdencent,ydescent,width,height,fontsize,trans):
        center = 0.5*width-0.5*xdencent,0.5*height-0.5*ydescent
        p = m_patches.Ellipse(xy=center,width=width+xdencent,height=height+xdencent)
        self.update_prop(p,orig_handle,legend)
        p.set_transform(trans)
        return [p]
c = m_patches.Circle((0.5,0.5),0.25,facecolor='green',edgecolor='red',linewidth=3)
plt.gca().add_patch(c)
plt.legend([c],['An ellipse,not a rectangle'],handler_map={m_patches.Circle:HandlerEllipse()})
plt.show()