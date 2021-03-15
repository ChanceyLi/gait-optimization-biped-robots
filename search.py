import numpy as np
import math


def search(S1,H_p):
    #t = np.arange(0,0.8,0.001)
    size = 800
    T = 0.8
    t_p = 0.4
    S = 0.3
    S_p = S
    l1 = 0.32
    l2 = 0.32
    H = 0.56
    A_x = np.array([[0,0,0,0,1],[t_p**4,t_p**3,t_p**2,t_p,1],[T**4,T**3,T**2,T,1],[0,0,0,1,0],[4*T**3,3*T**2,2*T,1,0]])
    b_x = np.array([-S,-S+S_p,S,0,0])
    [a4,a3,a2,a1,a0] = np.linalg.solve(A_x,b_x)
    b_z = np.array([0,H_p,0,0,0])
    [b4,b3,b2,b1,b0] = np.linalg.solve(A_x,b_z)

    S2 = 0.15 - S1
    A_h = np.array([[0,0,0,0,1],[(t_p)**4,(t_p)**3,(t_p)**2,t_p,1],[T**4,T**3,T**2,T,1],[4*T**3,3*T**2,2*T,0,0],[12*T**2,6*T,4,0,0]])
    b_h = np.array([-S1,S2,S-S1,0,0])
    [c4,c3,c2,c1,c0] = np.linalg.solve(A_h,b_h) 
    x_f = []
    z_f = []
    x_h = []
    z_h = []
    for i in range(size):
        x_f.append(funploy(a0,a1,a2,a3,a4,i / 1000))
        z_f.append(funploy(b0,b1,b2,b3,b4,i / 1000))
        x_h.append(funploy(c0,c1,c2,c3,c4,i / 1000))
        z_h.append(H)


    x_m = []
    z_m = []
    for i in range(size):
        x_m.append(funmid(x_f[i],z_f[i],x_h[i],z_h[i],l1,l2)[0])
        z_m.append(funmid(x_f[i],z_f[i],x_h[i],z_h[i],l1,l2)[1])
    x_l = np.zeros(size,)
    z_l = np.zeros(size,)
    x_l = list(x_l)
    z_l = list(z_l)
    x_m2 = []
    z_m2 = []
    for i in range(size):
        x_m2.append(funmid(x_l[i],z_l[i],x_h[i],z_h[i],l1,l2)[0])
        z_m2.append(funmid(x_l[i],z_l[i],x_h[i],z_h[i],l1,l2)[1])
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
    return modzmp

def funploy(a0,a1,a2,a3,a4,t):
    return a4*t**4+a3*t**3+a2*t**2+a1*t+a0

def funmid(x_f,z_f,x_h,z_h,l1,l2):
    l = math.sqrt((x_f - x_h)**2 + (z_f - z_h)**2)
    alpha = math.acos((x_h - x_f) / l)
    theta = math.acos((l**2 + l1**2 - l2**2)/(2*l*l1))
    [x_m,z_m] = [x_f + l1*math.cos(alpha - theta), z_f + l1*math.sin(alpha - theta)]
    return [x_m,z_m]
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
res, S1_search, H_p_search = 10000, 0, 0
size = 800
for i in range(int(size / 8)):
    for j in range(int(size / 80)):
        S1 = 0.05 + 0.1 * i * 8 / size
        H_p = 0.05
        modzmp = search(S1,H_p)
        if res > modzmp:
            S1_search = S1
            H_p_search = H_p
            res = modzmp
print([S1_search, H_p_search]) 