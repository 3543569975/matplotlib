import matplotlib.pyplot
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,30,33,60]
plt.plot(x,y,color='r',linestyle='-',marker = 'o',markerfacecolor = 'w')

plt.rcParams['font.sans-serif'] = ['SimHei']#处理中文
#x坐标轴名称
plt.xlabel('时间')
plt.ylabel('温度')
month = (str(i)+'月' for i in range(1,7))
#x坐标轴刻度
plt.xticks(range(1,7),month)
#y坐标轴刻度
plt.yticks(range(1,70,10))

#坐标轴范围
plt.xlim(1,10)
plt.ylim(1,80)
plt.grid(color='b',linestyle=':',linewidth='1',axis='x')#隐藏x轴网格线
plt.show()