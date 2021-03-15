import math
import numpy
import matplotlib.pyplot as plt
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

def list_add_d(a,b):
    c = []
    for i in range(len(a)):
        c.append((a[i]+b[i])/2)
    return c

def funax(a,t_sample):
    res = []
    for i in range(len(a) - 2):
        res.append((a[i + 2] + a[i] - 2*a[i + 1])/ t_sample**2)
    res.append(res[len(res) - 1])
    res.append(res[len(res) - 1])
    return res

def funzmp(x,z,ax,az,m,g):
    mol,den = 0,0
    for i in range(len(x)):
        mol += m[i]*((az[i]+g)*x[i] - ax[i]*z[i])
        den += m[i]*(az[i]+g)
    return mol / den

t_sample = 0.001
g = 9.81
m1,m2,m3,m4,m5,m6,m7=1.52,1.68,2.68,10.45,2.68,1.68,1.52
x1 = x_l
z1 = []
for i in range(size):
    z1.append(-0.04)
x2 = list_add_d(x_l,x_m2)
z2 = list_add_d(z_l,z_m2)
x3 = list_add_d(x_m2,x_h)
z3 = list_add_d(z_m2,z_h)
x4 = x_h
z4 = []
for i in range(size):
    z4.append(z_h[i] + 0.12)
x5 = list_add_d(x_h,x_m)
z5 = list_add_d(z_h,z_m)
x6 = list_add_d(x_m,x_f)
z6 = list_add_d(z_m,z_f)
x7 = x_f
z7 = []
for i in range(size):
    z7.append(z_f[i] - 0.04)
ax1 = funax(x1,t_sample)
ax2 = funax(x2,t_sample)
ax3 = funax(x3,t_sample)
ax4 = funax(x4,t_sample)
ax5 = funax(x5,t_sample)
ax6 = funax(x6,t_sample)
ax7 = funax(x7,t_sample)
az1 = funax(z1,t_sample)
az2 = funax(z2,t_sample)
az3 = funax(z3,t_sample)
az4 = funax(z4,t_sample)
az5 = funax(z5,t_sample)
az6 = funax(z6,t_sample)
az7 = funax(z7,t_sample)

x_zmp = []

for i in range(size):
    x = [x1[i],x2[i],x3[i],x4[i],x5[i],x6[i],x7[i]]
    z = [z1[i],z2[i],z3[i],z4[i],z5[i],z6[i],z7[i]]
    ax = [ax1[i],ax2[i],ax3[i],ax4[i],ax5[i],ax6[i],ax7[i]]
    az = [az1[i],az2[i],az3[i],az4[i],az5[i],az6[i],az7[i]]
    m = [m1,m2,m3,m4,m5,m6,m7]
    tmp = funzmp(x,z,ax,az,m,g)
    x_zmp.append(tmp)

modzmp = 0
for i in range(size):
    modzmp += (abs(x_zmp[i]) > 0.12)

fig = plt.figure(1)
ax = fig.add_subplot(1,1,1)
ax.plot(t,x_zmp,color = 'r')
plt.show()