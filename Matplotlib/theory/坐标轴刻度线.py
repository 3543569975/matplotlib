import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,30,33,60]

plt.plot(x,y,marker = 'o')
for a,b in zip(x,y):
    plt.text(a,b,b,ha='center',va = 'bottom',fontsize = 12,color = 'r')
plt.rcParams['font.sans-serif'] = ['SimHei']

#设置间距
plt.subplots_adjust(left = 0.2,right = 0.9,top = 0.9,bottom = 0.2)

#设置是否显示坐标轴刻度线
#plt.tick_params(bottom = True,left = True,right = True,top = False)

#设置坐标走刻度线显示方向
plt.rcParams['xtick.direction']= 'in'
plt.rcParams['ytick.direction']= 'in'
plt.show()