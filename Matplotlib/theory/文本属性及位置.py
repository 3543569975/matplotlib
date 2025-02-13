import matplotlib.pyplot as plt
import matplotlib.patches as patches


#使用text（）可以显示各种对齐方式
left,width = 0.25,0.5
bottom,height = 0.25,.5
right = left+width
top = bottom+height
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
p = patches.Rectangle((left,bottom),width,height,fill=False,transform=ax.transAxes,clip_on=False)
ax.add_patch(p)
ax.text(left,bottom,'left top',horizontalalignment = 'left',verticalalignment = 'top',transform = ax.transAxes)
ax.text(left,bottom,'left bottom',horizontalalignment = 'left',verticalalignment = 'bottom',transform = ax.transAxes)
ax.text(right,top,'right top',horizontalalignment = 'right',verticalalignment = 'bottom',transform = ax.transAxes)
ax.text(right,top,'right top',horizontalalignment = 'right',verticalalignment = 'top',transform = ax.transAxes)
ax.text(right,bottom,'center top',horizontalalignment = 'center',verticalalignment = 'top',transform = ax.transAxes)
ax.text(left,0.5*(bottom+top),'right center',horizontalalignment = 'right',verticalalignment = 'center',
        rotation = 'vertical',transform = ax.transAxes)
ax.text(left,0.5*(bottom+top),'left center',horizontalalignment = 'left',verticalalignment = 'center',
        rotation = 'vertical',transform = ax.transAxes)
ax.text(0.5*(left+right),0.5*(bottom+top),'middle',horizontalalignment = 'center',verticalalignment = 'center',
        fontsize = 20,color = 'r',transform = ax.transAxes)
ax.text(right,0.5*(bottom+top),'centered',horizontalalignment = 'center',verticalalignment = 'center',
        rotation = 'vertical',transform = ax.transAxes)
ax.text(left,top,'rotated\nwith newlines',horizontalalignment = 'center',verticalalignment = 'center',
        rotation = 45,transform = ax.transAxes)
ax.set_axis_off()
plt.show()