from parameter import t
from parameter import x_f
from parameter import z_f
from parameter import x_h
from parameter import z_h
from parameter import x_m
from parameter import z_m
import matplotlib.pyplot as plt
fig1 = plt.figure(1)
ax1 = fig1.add_subplot(1,2,1)
ax2 = fig1.add_subplot(1,2,2)
ax1.plot(t,x_f,color = 'r')
ax1.plot(t,z_f,color = 'b')
ax1.plot(t,x_h,color = 'g')
ax2.plot(x_f,z_f,color = 'r')
ax2.plot(x_h,z_h,color = 'b')
ax2.plot(x_m,z_m,color = 'g')
ax1.set_xlabel('t',  fontsize = 15)
ax1.set_ylabel('l',  fontsize = 15)
ax2.set_xlabel('x',fontsize = 15)
ax2.set_ylabel('z',fontsize = 15)
plt.show()