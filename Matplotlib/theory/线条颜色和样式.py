import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,30,33,60]
plt.plot(x,y,color='r',linestyle='-',marker = 'o',markerfacecolor = 'w')
#灰度值0-1，b蓝，g绿，r红，c蓝绿色，m洋红，y黄，k黑，w白
#-实线,--双划线,-.点画线,:虚线
#.点标记，，像素标记，o实心圆标记，v倒三角标记，^上三角标记，>右三角，<左三角，1234下上左右花三角标记，s实心正方形，p实心五角形标记，*星形
#markerfacecolor = 'w',简写mfc
plt.show()