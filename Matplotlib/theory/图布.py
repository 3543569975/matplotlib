import matplotlib.pyplot
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,30,33,60]
plt.figure(num=2,figsize=(10,6),dpi=100,facecolor='y',edgecolor='m',frameon=True)
plt.plot(x,y,color='r',linestyle='-',marker = 'o',markerfacecolor = 'w')

plt.show()
'''
num:图像编号或名称，数字为编号，字符串为名称，可以通过该参数激活不同的画布
figsize：画布的宽和高，单位英寸
dpi：绘图对象的分辨率，每英寸包含多少个像素，默认值80，越大画布越大
facecolor：背景颜色
edgcolor：边框颜色
frameon：是否显示边框，默认值为True，绘制边框，False：不绘制边框
'''