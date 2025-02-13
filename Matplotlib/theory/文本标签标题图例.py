import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,30,33,60]

plt.plot(x,y,color='b',linestyle='-',marker = 'o',markerfacecolor = 'w')

plt.rcParams['font.sans-serif'] = ['SimHei']#处理中文

#x坐标轴名称
plt.xlabel('时间')
plt.ylabel('温度')

#文本标签
for a,b in zip(x,y):
    plt.text(a,b,b,ha='center',va = 'bottom',fontsize = 15,color = 'b')

x = [0,2,4,6]
y = [55,45,15,5]
plt.plot(x,y,color='r',linestyle='--',marker = 'o',markerfacecolor = 'w')
plt.title('图表的标题',fontsize= 15)
for a,b in zip(x,y):
    plt.text(a,b,b,ha='center',va = 'bottom',fontsize = 15,color = 'r')
#图例
plt.legend(('1','2'))


plt.show()