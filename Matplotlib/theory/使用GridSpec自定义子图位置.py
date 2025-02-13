import matplotlib.pyplot as plt
import matplotlib.gridspec as grid_spec

#subplot2grid
ax = plt.subplot2grid((2,2),(0,0))#==  ax = plt.subplot(2,2,1)
#创建跨越多个网格的子图
ax_2 = plt.subplot2grid((3,3),(1,0),colspan=2)
ax_3 = plt.subplot2grid((3,3),(1,2),rowspan=2)
plt.show()

ax_1 = plt.subplot2grid((3,3),(0,0),colspan=3)
ax_2 = plt.subplot2grid((3,3),(1,0),colspan=2)
ax_3 = plt.subplot2grid((3,3),(1,2),rowspan=2)
ax_4 = plt.subplot2grid((3,3),(2,0))
ax_5 = plt.subplot2grid((3,3),(2,1))
plt.show()

#GridSpec和SubplotSpec
gs = grid_spec.GridSpec(3,3)
ax1 = plt.subplot(gs[0,:])
ax2 = plt.subplot(gs[1,:-1])
ax3 = plt.subplot(gs[1:,-1])
ax4 = plt.subplot(gs[-1,0])
ax5 = plt.subplot(gs[-1,-3])
plt.show()