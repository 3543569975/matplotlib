import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,30,33,60]

plt.plot(x,y,marker = 'o')
for a,b in zip(x,y):
    plt.text(a,b,b,ha='center',va = 'bottom',fontsize = 12,color = 'r')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.annotate('1',xy = (4,33),xytext = (0,-100),textcoords='offset points',fontsize = 16,
             arrowprops = dict(arrowstyle = '<->',connectionstyle = 'arc3,rad =.2'))
#arrowprops = dict(facecolor = 'r',shrink = 0.05)
#xytext = (0,-100)到点的距离
plt.show()
