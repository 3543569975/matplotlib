import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
df = pd.read_excel('成绩.xlsx')
plt.rcParams['font.sans-serif'] = ['SimHei']

x = df['姓名']
y1 = df['语文']
y2 = df['数学']
y3 = df['英语']

#设置画布大小
plt.figure(figsize=(10,6))

#设置网格线
plt.grid(axis='y')

plt.plot(x,y1,color='r',linestyle='-',marker = 'o')
plt.plot(x,y2,color='b',linestyle='--',marker = 'o')
plt.plot(x,y3,color='k',linestyle=':',marker = 'o')

plt.title('成绩',fontsize= 15)

#设置图例
plt.legend(['语文','数学','英语'])

#设置坐标轴刻度
plt.yticks(range(0,150,10))

plt.xlabel('姓名')
plt.ylabel('成绩')
plt.show()