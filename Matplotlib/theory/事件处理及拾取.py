import matplotlib.pyplot as plt
import numpy as np


#事件连接
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(np.random.rand(10))
def onclick(event):
    print('发生点击操作：button={},x={},y={},xdata={},ydata={}'.
          format(event.button,event.x,event.y,event.xdata,event.ydata))
cid = fig.canvas.mpl_connect('button_press_event',onclick)
plt.show()

#事件属性
class LineBuilder:
    def __init__(self,line_v):
        self.line = line_v
        self.xs = list(line_v.get_xdata())
        self.ys = list(line_v.get_ydata())
        self.cid = line_v.figure.canvas.mpl_connect('button_press_event',self)
    def __call__(self,event):
        print('点击输出：{}'.format(event))
        if event.inaxes != self.line.axes: return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.line.set_data(self.xs,self.ys)
        self.line.figure.canvas.draw()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('click to build line segment')
line, = ax.plot([0], [0])
line_builder = LineBuilder(line)
plt.show()

#可拖曳矩形
class DraggableRectangle:
    lock = None
    def __init__(self,rect):
        self.rect = rect
        self.press = None
        self.background = None
    def connect(self):
        'connect to all the events we need'
        self.cidpress = self.rect.figure.canvas.mpl_connect('button_press_event',self.on_press)
        self.cidrelease = self.rect.figure.canvas.mpl_connect('button_press_event',self.on_release)
        self.cidmotion = self.rect.figure.canvas.mpl_connect('motion_notify_event',self.on_motion)
    def on_press(self,event):
        'on button press we will see if the mouse is over us and store some data'
        if event.inaxes != self.rect.axes:return
        if DraggableRectangle.lock is not None:return
        contains,attrd = self.rect.contains(event)
        if not contains:return
        print('event contains:{}'.format(self.rect.xy))
        x0,y0 = self.rect.xy
        self.press = x0,y0,event.xdata,event.ydata
        DraggableRectangle.lock = self

        canvas = self.rect.figure.canvas
        axes = self.rect.axes
        self.rect.set_animated(True)
        canvas.draw()
        self.background = canvas.copy_from_bbox(self.rect.axes.bbox)
        axes.draw_artist(self.rect)
        canvas.blit(axes.bbox)
    def on_motion(self,event):
        'on motion we will move the rect if the mouse is over us'
        if DraggableRectangle.lock is not self:
            return
        if event.inaxes != self.rect.axes:return
        x0,y0,xpress,ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        self.rect.set_x(x0+dx)
        self.rect.set_y(y0+dy)
        canvas = self.rect.figure.canvas
        axes = self.rect.axes
        canvas.restore_regiono(self.background)
        axes.draw_artist(self.rect)
        canvas.blit(axes.bbox)
    def on_release(self,event):
        'on release we reser the press data'
        if DraggableRectangle.lock is not self:
            return
        self.press = None
        self.press = None
        DraggableRectangle.lock = None
        self.rect.set_animated(False)
        self.background = None
        self.rect.figure.canvas.draw()
    def disconnect(self):
        'disconnect all the stored connection ids'
        self.rect.figure.canvas.mpl_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl_disconnect(self.cidrelease)
        self.rect.figure.canvas.mpl_disconnect(self.cidmotion)
fig = plt.figure()
ax =fig.add_subplot(111)
rects = ax.bar(range(10),20*np.random.rand(10))
drs = []
for rect in rects:
    dr = DraggableRectangle(rect)
    dr.connect()
    drs.append(dr)
plt.show()

#鼠标进入与离开
def enter_axes(event):
    print('enter_axes:{}'.format(event.inaxes))
    event.inaxes.patch.set_facecolor('yellow')
    event.canvas.draw()
def leave_axes(event):
    print('leave_axes:{}'.format(event.inaxes))
    event.inaxes.patch.set_facecolor('white')
    event.canvas.draw()
def enter_figure(event):
    print('enter_figure:{}'.format(event.canvas.figure))
    event.canvas.figure.patch.set_facecolor('r')
    event.canvas.draw()
def leave_figure(event):
    print('leave_figure:{}'.format(event.canvas.figure))
    event.canvas.figure.patch.set_facecolor('grey')
    event.canvas.draw()
fig1 = plt.figure()
fig1.suptitle('mouse hover over figure or axes to trigger events')
ax1 = fig1.add_subplot(211)
ax2 = fig1.add_subplot(212)
fig1.canvas.mpl_connect('figure_enter_event',enter_figure)
fig1.canvas.mpl_connect('figure_leave_event',leave_figure)
fig1.canvas.mpl_connect('axes_enter_event',enter_axes)
fig1.canvas.mpl_connect('axes_leave_event',leave_axes)
plt.show()

#对象拾取
X = np.random.rand(100,1000)
xs = np.mean(X,axis=1)
ys = np.std(X,axis=1)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('click on point to plot time series')
line, = ax.plot(xs,ys,'o',picker=5)
def on_pick(event):
    if event.artist != line:return True
    ind_len = len(event.ind)
    if not ind_len:return True
    fi_gi = plt.figure()
    for sub_polt_num,data_ind in enumerate(event.ind):
        ax = fi_gi.add_subplot(ind_len,1,sub_polt_num+1)
        ax.plot(X[data_ind])
        ax.text(0.05,0.9,'mu=%1.3f\nsigma=%1.3f' % (xs[data_ind],ys[data_ind]),transform=ax.transAxes,va='top')
        ax.set_ylim(-0.5,1.5)
    fi_gi.show()
    return True
fig.canvas.mpl_connect('pick_event',on_pick)
plt.show()