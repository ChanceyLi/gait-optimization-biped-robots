run data.m

[a0,a1,a2,a3,a4,a5,a6,b0,b1,b2,b3,b4,b5]=solveMF(xs,zs,...
    xh,zh,xf,zf,ts,th,tf);
tsample=(tf-ts)/N;
xln=zeros(1,N+1);
zln=zeros(1,N+1);
x01n=zeros(1,N+1);
y01n=zeros(1,N+1);
z01n=zeros(1,N+1);
x12n=zeros(1,N+1);
y12n=zeros(1,N+1);
z12n=zeros(1,N+1);
x234n=zeros(1,N+1);
y234n=zeros(1,N+1);
z234n=zeros(1,N+1);
x45n=zeros(1,N+1);
y45n=zeros(1,N+1);
z45n=zeros(1,N+1);
x56n=zeros(1,N+1);
y56n=zeros(1,N+1);
z56n=zeros(1,N+1);
x01n(1)=x01;
y01n(1)=y01;
z01n(1)=z01;
x12n(1)=x12;
y12n(1)=y12;
z12n(1)=z12;
x234n(1)=x234;
y234n(1)=y234;
z234n(1)=z234;
x45n(1)=x45;
y45n(1)=y45;
z45n(1)=z45;
x56n(1)=x56;
y56n(1)=y56;
z56n(1)=z56;
for i = 2 : N+1
    t=(i-1)*tsample;
    xln(i)=a0+a1*t+a2*t^2+a3*t^3+a4*t^4+a5*t^5+a6*t^6;
    zln(i)=b0+b1*t+b2*t^2+b3*t^3+b4*t^4+b5*t^5;
    x01b=x01*(i-1);
    y01b=y01*(i-1);
    z01b=z01*(i-1);
    x12b=x12*(i-1);
    y12b=y12*(i-1);
    z12b=z12*(i-1);
    x234b=x234*(i-1);
    y234b=y234*(i-1);
    z234b=z234*(i-1);
    x45b=x45*(i-1);
    y45b=y45*(i-1);
    z45b=z45*(i-1);
    x56b=x56*(i-1);
    y56b=y56*(i-1);
    z56b=z56*(i-1);
    if i <= 2
        x01bb=x01*(i-1);
        y01bb=y01*(i-1);
        z01bb=z01*(i-1);
        x12bb=x12*(i-1);
        y12bb=y12*(i-1);
        z12bb=z12*(i-1);
        x234bb=x234*(i-1);
        y234bb=y234*(i-1);
        z234bb=z234*(i-1);
        x45bb=x45*(i-1);
        y45bb=y45*(i-1);
        z45bb=z45*(i-1);
        x56bb=x56*(i-1);
        y56bb=y56*(i-1);
        z56bb=z56*(i-1);
    else
        x01bb=x01*(i-2);
        y01bb=y01*(i-2);
        z01bb=z01*(i-2);
        x12bb=x12*(i-2);
        y12bb=y12*(i-2);
        z12bb=z12*(i-2);
        x234bb=x234*(i-2);
        y234bb=y234*(i-2);
        z234bb=z234*(i-2);
        x45bb=x45*(i-2);
        y45bb=y45*(i-2);
        z45bb=z45*(i-2);
        x56bb=x56*(i-2);
        y56bb=y56*(i-2);
        z56bb=z56*(i-2);
    end
        [x0,y0,z0,x1,y1,z1,x2,y2,z2,x3,y3,z3,...
          x4,y4,z4,x5,y5,z5,x6,y6,z6]...
          =solveGC1(xln(i),yl,zln(i),x01n(i),y01n(i),z01n(i),x12n(i),y12n(i),z12n(i),x234n(i),y234n(i),z234n(i),...
                   x45n(i),y45n(i),z45n(i),x56n(i),y56n(i),z56n(i),xr,yr,zr,...
                   mu0,mu1,mu2,mu4,mu5,mu6,l3);
        [x0b,y0b,z0b,x1b,y1b,z1b,x2b,y2b,z2b,x3b,y3b,z3b,...
          x4b,y4b,z4b,x5b,y5b,z5b,x6b,y6b,z6b]...
          =solveGC1(xln(i),yl,zln(i),x01b,y01b,z01b,x12b,y12b,z12b,x234b,y234b,z234b,...
                   x45b,y45b,z45b,x56b,y56b,z56b,xr,yr,zr,...
                   mu0,mu1,mu2,mu4,mu5,mu6,l3); 
        [x0bb,y0bb,z0bb,x1bb,y1bb,z1bb,x2bb,y2bb,z2bb,x3bb,y3bb,z3bb,...
          x4bb,y4bb,z4bb,x5bb,y5bb,z5bb,x6bb,y6bb,z6bb]...
          =solveGC1(xln(i),yl,zln(i),x01bb,y01bb,z01bb,x12bb,y12bb,z12bb,x234bb,y234bb,z234bb,...
                   x45bb,y45bb,z45bb,x56bb,y56bb,z56bb,xr,yr,zr,...
                   mu0,mu1,mu2,mu4,mu5,mu6,l3); 
        [x_zmp,y_zmp] = solveZMP(x0,y0,z0,x0b,y0b,z0b,x0bb,y0bb,z0bb,...
                                 x1,y1,z1,x1b,y1b,z1b,x1bb,y1bb,z1bb,...
                                 x2,y2,z2,x2b,y2b,z2b,x2bb,y2bb,z2bb,...
                                 x3,y3,z3,x3b,y3b,z3b,x3bb,y3bb,z3bb,...
                                 x4,y4,z4,x4b,y4b,z4b,x4bb,y4bb,z4bb,...
                                 x5,y5,z5,x5b,y5b,z5b,x5bb,y5bb,z5bb,...
                                 x6,y6,z6,x6b,y6b,z6b,x6bb,y6bb,z6bb,...
                                 m0,m1,m2,m3,m4,m5,m6,g,N,tf,ts);
        func=(x_zmp-xr)^2+(y_zmp-yr)^2;
end

