import numpy as np
import matplotlib.pyplot as plt


#对数和其他非线性轴
#更改轴的刻度
plt.xscale('log')
#生成一些[0,1]内的数据
y = np.random.normal(loc=0.5,scale=0.4,size=1000)
y = y[(y>0)&(y<1)]
y.sort()
x = np.arange(len(y))
#带有多个轴域刻度的plot
plt.figure(1)
#线性
plt.subplot(221)
plt.plot(x,y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)
#对数
plt.subplot(222)
plt.plot(x,y)
plt.yscale('log')
plt.title('log')
plt.grid(True)
#对数的对数
plt.subplot(223)
plt.plot(x,y-y.mean())
plt.yscale('symlog',linthreshy=0.05)
plt.title('symlog')
plt.grid(True)
#logit
plt.subplot(224)
plt.plot(x,y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)
plt.show()