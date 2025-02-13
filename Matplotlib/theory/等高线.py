import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    return (x**2+y**2)

n = 4

x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)

plt.contourf(X,Y,f(X,Y),8,alpha = 0.75,cmap = plt.cm.hot)

C = plt.contour(X,Y,f(X,Y),8,colors='black')

plt.clabel(C,inline=True,fontsize=10)

plt.xticks(())
plt.yticks(())
plt.show()