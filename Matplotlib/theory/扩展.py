import matplotlib.pyplot as plt
import numpy as np


#透明度填充
n_step, n_walker = 100,250
t = np.arange(n_step)
s1 = 0.002+0.01*np.random.randn(n_step,n_walker)
s2 = 0.004+0.02*np.random.randn(n_step,n_walker)
x1 = s1.cumsum(axis=0)
x2 = s2.cumsum(axis=0)
mu1 = x1.mean(axis=1)
sigma1 = x1.std(axis=1)
mu2 = x2.mean(axis=1)
sigma2 = x2.std(axis=1)
fig,ax = plt.subplots(1)
ax.plot(t,mu1,lw = 2,label='mean population 1',color='blue')
ax.plot(t,mu2,lw=2,label='mean population 2',color='yellow')
ax.fill_between(t,mu1+sigma1,mu1-sigma1,facecolor='b',alpha=0.5)
ax.fill_between(t,mu2+sigma2,mu2-sigma2,facecolor='y',alpha=0.5)
ax.set_title('random walkers empirical $\mu$ and $\pm \sigma$ interval')
ax.legend(loc='upper left')
ax.set_xlabel('num steps')
ax.set_ylabel('position')
ax.grid()
plt.show()

#透明、花式图例
np.random.seed(1234)
fig,ax = plt.subplots(1)
ax.plot(np.random.randn(300),'o-',label='normal distribution')
ax.plot(np.random.randn(300),'s-',label='uniform distribution')
ax.set_ylim(-3,3)
ax.legend(loc='best',fancybox=True,framealpha=0.5)
ax.set_title('fancy, transparent legends')
plt.show()

#放置文本框
np.random.seed(1234)
fig,ax = plt.subplots(1)
x = 30*np.random.randn(10000)
mu = x.mean()
median = np.median(x)
sigma = x.std()
text_str = '$\mu=%.2f$\n$\mathrm{median}=%.2f$\n$sigma=%.2f$' % (mu,median,sigma)
ax.hist(x,50)
props = dict(boxstyle = 'round',facecolor='wheat',alpha=0.5)
ax.text(0.05,0.95,text_str,transform=ax.transAxes,fontsize=14,
        verticalalignment='top',bbox=props)
plt.show()