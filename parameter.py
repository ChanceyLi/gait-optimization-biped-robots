#reference:E:\lenovo\Documents\复杂控制实验室\相关论文\GAmethod.pdf
import numpy as np
import math
#consider t : 0 -> T
t = np.arange(0,0.8,0.001)
def funploy(a0,a1,a2,a3,a4,t):
    return a4*t**4+a3*t**3+a2*t**2+a1*t+a0
def funployh(a0,a1,a2,a3,a4,a5,a6,a7,t):
    return a7*t**7+a6*t**6+a5*t**5+a4*t**4+a3*t**3+a2*t**2+a1*t+a0
size = 800
T = 0.8
t_p = 0.4
S = 0.3
S_p = S
H_p = 0.05
H = 0.60 # H <sqrt((l1+l2)^2-(S-S1)^2)
l1 = 0.32
l2 = 0.32
A_x = np.array([[0,0,0,0,1],[t_p**4,t_p**3,t_p**2,t_p,1],[T**4,T**3,T**2,T,1],[0,0,0,1,0],[4*T**3,3*T**2,2*T,1,0]])
b_x = np.array([-S,-S+S_p,S,0,0])
[a4,a3,a2,a1,a0] = np.linalg.solve(A_x,b_x)
b_z = np.array([0,H_p,0,0,0])
[b4,b3,b2,b1,b0] = np.linalg.solve(A_x,b_z)


#############顶部位置
S1 = 0.1362
S2 = 0.15 - S1
A_h = np.array([[0,0,0,0,1],[(t_p)**4,(t_p)**3,(t_p)**2,t_p,1],[T**4,T**3,T**2,T,1],[4*T**3,3*T**2,2*T,0,0],[12*T**2,6*T,4,0,0]])
b_h = np.array([-S1,S2,S-S1,0,0])
[c4,c3,c2,c1,c0] = np.linalg.solve(A_h,b_h)
c2,c6,c7 = -0.9609,-0.9453,-1.002
m1 = S-c7*T**7-c6*T**6-c2*T**2
m2 = S1 + S2 - c7*t_p**7-c6*t_p**6-c2*t_p**2
m3 = -7*c7*T**6-6*c6*T**5-2*c2*T
m4 = -42*c7*T**5-30*c6*T**4-4*c2
c5 = -32*(m2-m1/2+3*m3*T/16-m4*T**2/32)/(5*T**5)
c4 = (m4-2*m3/T-10*T**3*c5)/(4*T**2)
c3 = (m3 - 5*T**4*c5-4*T**3*c4)/(3*T**2)
c1 = (m1-T**5*c5-T**4*c4-T**3*c3)/T
c0 = -S1
#############移动脚位置
x_f = []
z_f = []
x_h = []
z_h = []
for i in range(size):
    x_f.append(funploy(a0,a1,a2,a3,a4,i / 1000))
    z_f.append(funploy(b0,b1,b2,b3,b4,i / 1000))
    x_h.append(funployh(c0,c1,c2,c3,c4,c5,c6,c7,i / 1000))
    z_h.append(H)

def funmid(x_f,z_f,x_h,z_h,l1,l2):
    l = math.sqrt((x_f - x_h)**2 + (z_f - z_h)**2)
    alpha = math.acos((x_h - x_f) / l)
    theta = math.acos((l**2 + l1**2 - l2**2)/(2*l*l1))
    [x_m,z_m] = [x_f + l1*math.cos(alpha - theta), z_f + l1*math.sin(alpha - theta)]
    return [x_m,z_m]
x_m = []
z_m = []
for i in range(size):
    x_m.append(funmid(x_f[i],z_f[i],x_h[i],z_h[i],l1,l2)[0])
    z_m.append(funmid(x_f[i],z_f[i],x_h[i],z_h[i],l1,l2)[1])

###########固定脚位置
x_l = np.zeros(size,)
z_l = np.zeros(size,)
x_l = list(x_l)
z_l = list(z_l)
x_m2 = []
z_m2 = []

for i in range(size):
    x_m2.append(funmid(x_l[i],z_l[i],x_h[i],z_h[i],l1,l2)[0])
    z_m2.append(funmid(x_l[i],z_l[i],x_h[i],z_h[i],l1,l2)[1])
#print(a0,a1,a2,a3,a4)
#print(b0,b1,b2,b3,b4)
#print(c0,c1,c2,c3,c4)