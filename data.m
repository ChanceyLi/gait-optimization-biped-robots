%存储机器人所有的初始数据

%连杆质量(kg)
m0=1;m1=1;m2=1;m3=1;m4=1;m5=1;m6=1;

%连杆长度(m)
l0=0.1;l1=0.1;l2=0.1;l3=0.1;l4=0.1;l5=0.1;l6=0.1;

%质心相对位置，mu=0.3表示质心位于从连杆底部往上mu*l长的位置
mu0=0.5;mu1=0.5;mu2=0.5;mu3=1;mu4=0.5;mu5=0.5;mu6=0.5;

%重力加速度(m/s2)
g=9.81;

%机器人初始姿态坐标
xl=0;yl=0;zl=0;
x01=0;y01=0;z01=0.1;
x12=0;y12=0.05;z12=0.1866;
x234=0;y234=0.1;z234=0.2732;
x45=0;y45=0.15;z45=0.1866;
x56=0;y56=0.2;z56=0.1;
xr=0;yr=0.2;zr=0;

%初始时刻以及运动脚路径数据,t的单位为秒/s
xs=xl;ys=yl;zs=zl;ts=0;
xh=0.02;yh=0;zh=0.01;th=1;
xf=0.04;yf=0;zf=0;tf=2;

%采样点数
N=200;

%脚掌大小
lx=0.05;ly=0.05;