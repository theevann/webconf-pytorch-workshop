import torch
import numpy as np

from IPython.display import HTML
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams.update({'figure.max_open_warning': 0})


def anim_2d(x_range, func, data, delta=500):
    iterations = len(data)
    
    fig = plt.figure();
    ax = fig.gca()
    
    y = func(x_range)
    ax.plot(x_range.numpy(), y.numpy(), 'b')
    scat = ax.scatter([], [], vmin=0, vmax=1, cmap="jet", edgecolor="k", c="r")
#     scat, = ax.plot([], [], '-o', c='r')
    
    def animate(i):
        scat.set_offsets(data[:i])
#         scat.set_data(zip(*data[:i]))
        return scat,

    anim = animation.FuncAnimation(fig, animate, np.arange(1, iterations), interval=delta, blit=True, repeat=False)
    return HTML(anim.to_html5_video())


def anim_3d(x_range, y_range, elev, azim, func, data, delta=500):
    iterations = len(data)
    data = np.array(data).T

    fig = plt.figure(figsize=(8, 6), dpi=120)
    ax = fig.gca(projection='3d')
    ax.view_init(elev=elev, azim=azim)

    X, Y = torch.meshgrid([x_range, y_range])
    Z = func(X, Y).numpy()
    ax.plot_wireframe(X.numpy(), Y.numpy(), Z, linewidth=.005, antialiased=False)
    scat = ax.scatter3D([], [], [], s=30, c='r', edgecolor='k', linewidth=.5, depthshade=False)

    def animate(i):
        scat._offsets3d = (*data[:, :i], )
        return scat,

    anim = animation.FuncAnimation(fig, animate, np.arange(1, iterations), interval=delta, blit=True, repeat=False)
    return HTML(anim.to_html5_video())