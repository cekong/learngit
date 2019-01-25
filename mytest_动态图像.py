''''''
'''
python绘制动态模拟图 https://blog.csdn.net/suzyu12345/article/details/78338091
动图的核心函数是matplotlib.animation.FuncAnimation:
anim = animation.funcanimation(fig, animate, init_func=init, frames=100, interval=20, blit=true)
# fig: 是我们创建的画布
# animat: 是重点，是我们每个时刻要更新图形对象的函数，返回值和init_func相同
# init_func: 初始化函数，其返回值就是每次都要更新的对象，
#    告诉FuncAnimation在不同时刻要更新哪些图形对象
# frames: 相当于时刻t，要模拟多少帧图画，不同时刻的t相当于animat的参数
# interval: 刷新频率，毫秒
# blit: blit是一个非常重要的关键字，它告诉动画只重绘修改的部分，结合上面保存的时间，
#    blit=true会使动画显示得会非常非常快
Animation 动画  https://morvanzhou.github.io/tutorials/data-manipulation/plt/5-1-animation/
'''


import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
fig.set_tight_layout(True)

# Query the figure's on-screen size and DPI. Note that when saving the figure to
# a file, we need to provide a DPI for that separately.
print('fig size: {0} DPI, size in inches {1}'.format(
    fig.get_dpi(), fig.get_size_inches()))

# Plot a scatter that persists (isn't redrawn) and the initial line.
x = np.arange(0, 20, 0.1)
ax.scatter(x, x + np.random.normal(0, 3.0, len(x)))
line, = ax.plot(x, x - 5, 'r-', linewidth=2)

def update(i):
    label = 'timestep {0}'.format(i)
    print(label)
    # Update the line and the axes (with a new xlabel). Return a tuple of
    # "artists" that have to be redrawn for this frame.
    line.set_ydata(x - 5 + i)
    ax.set_xlabel(label)
    return line, ax

if __name__ == '__main__':
    # FuncAnimation will call the 'update' function for each frame; here
    # animating over 10 frames, with an interval of 200ms between frames.
    anim = FuncAnimation(fig, update, frames=np.arange(0, 10), interval=200)
    if len(sys.argv) > 1 and sys.argv[1] == 'save':
        anim.save('line.gif', dpi=80, writer='imagemagick')
    else:
        # plt.show() will just loop the animation forever.
        plt.show()


