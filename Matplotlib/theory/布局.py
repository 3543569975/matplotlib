import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable

#tight_layout:自动调节子图参数，使之填充整个图像区域，检查坐标轴标签、刻度标签及标题部分。
arr = np.arange(100).reshape((10,10))
plt.close('all')
fig = plt.figure(figsize=(10,5))
ax = plt.subplot(111)
im = ax.imshow(arr,interpolation='none')
plt.tight_layout()
plt.show()

#颜色条
plt.close('all')
arr = np.arange(100).reshape((10,10))
fig = plt.figure(figsize=(4,4))
im = plt.imshow(arr,interpolation='none')
divider = make_axes_locatable(plt.gca())
cax = divider.append_axes('right','5%',pad='3%')
plt.colorbar(im,cax=cax)
plt.tight_layout()
plt.show()