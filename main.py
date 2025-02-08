import matplotlib.pyplot as plt 
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
import math
import random


fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection="3d")

def animate(f):
    ax.clear()
    k: int = 300

    x_tree: list[float] = [math.cos(i/5+f/10)*(k-i) for i in range(k)]
    y_tree: list[float] = [math.sin(i/5+f/10)*(k-i) for i in range(k)]
    z_tree: list[float] = [i for i in range(k)]
    ax.scatter(x_tree, y_tree, z_tree, c="green", marker="^")

    step: int = 3

    z_garland: list[float] = [i for i in range(1, k, step)]
    x_garland: list[float] = [math.cos(i/5+2+f/10)*(k-i+10) for i in range(1,k,step)]
    y_garland: list[float] = [math.sin(i/5+2+f/10)*(k-i+10) for i in range(1,k,step)]
    colors: list[str] = ["#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)]) for _ in range(len(z_garland))]
    ax.scatter(x_garland, y_garland, z_garland, c=colors, marker='o', s=40)

    ax.scatter([0], [0], [k], c="gold", marker="*", s=200)

    ax.set_xlim(-500, 500)
    ax.set_ylim(-500, 500)
    ax.set_zlim(0, k)

    ax.set_box_aspect([1,1,1])

    return fig,

ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)
ani.save(f"{__file__[:-7]}tree.gif")