import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from parameter import t
from parameter import x_f
from parameter import z_f
from parameter import x_h
from parameter import z_h
from parameter import x_m
from parameter import z_m
from parameter import x_l
from parameter import z_l
from parameter import x_m2
from parameter import z_m2
from parameter import size

speed = 4
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
line1, =ax.plot([x_f[0],x_m[0]],[z_f[0],z_m[0]])
line2, =ax.plot([x_h[0],x_m[0]],[z_h[0],z_m[0]])
line3, =ax.plot([x_l[0],x_m2[0]],[z_l[0],z_m2[0]])
line4, =ax.plot([x_h[0],x_m2[0]],[z_h[0],z_m2[0]])
ax.grid()
def init(): 
    line1.set_data([x_f[0],x_m[0]],[z_f[0],z_m[0]]) 
    line2.set_data([x_h[0],x_m[0]],[z_h[0],z_m[0]])
    line3.set_data([x_l[0],x_m2[0]],[z_l[0],z_m2[0]])  
    line4.set_data([x_h[0],x_m2[0]],[z_h[0],z_m2[0]])
    ax.set_xlim(x_f[0],2*x_f[799])
    ax.set_ylim(0,0.64)

def animate(i):
    tmp = 4 * i
    line1.set_data([x_f[tmp],x_m[tmp]],[z_f[tmp],z_m[tmp]])  
    line2.set_data([x_h[tmp],x_m[tmp]],[z_h[tmp],z_m[tmp]])
    line3.set_data([x_l[tmp],x_m2[tmp]],[z_l[tmp],z_m2[tmp]])  
    line4.set_data([x_h[tmp],x_m2[tmp]],[z_h[tmp],z_m2[tmp]])


ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=1, frames = int(size / speed), blit=False, repeat = True)
ani.save("test.gif", writer='pillow')
plt.show()