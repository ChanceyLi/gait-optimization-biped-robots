function [x0,y0,z0,x1,y1,z1,x2,y2,z2,x3,y3,z3,...
          x4,y4,z4,x5,y5,z5,x6,y6,z6]...
          =solveGC1(xl,yl,zl,x01,y01,z01,x12,y12,z12,x234,y234,z234,...
                   x45,y45,z45,x56,y56,z56,xr,yr,zr,...
                   mu0,mu1,mu2,mu4,mu5,mu6,l3)
    x0=mu0*xl+(1-mu0)*x01;
    y0=mu0*yl+(1-mu0)*y01;
    z0=mu0*zl+(1-mu0)*z01;
    x1=mu1*x01+(1-mu1)*x12;
    y1=mu1*y01+(1-mu1)*y12;
    z1=mu1*z01+(1-mu1)*z12; 
    x2=mu2*x12+(1-mu2)*x234;
    y2=mu2*y12+(1-mu2)*y234;
    z2=mu2*z12+(1-mu2)*z234;
    x3=x234;
    y3=y234;
    z3=z234+l3;
    x4=mu4*x234+(1-mu4)*x45;
    y4=mu4*y234+(1-mu4)*y45;
    z4=mu4*z234+(1-mu4)*z45;
    x5=mu5*x45+(1-mu5)*x56;
    y5=mu5*y45+(1-mu5)*y56;
    z5=mu5*z45+(1-mu5)*z56;
    x6=mu6*x56+(1-mu6)*xr;
    y6=mu6*y56+(1-mu6)*yr;
    z6=mu6*z56+(1-mu6)*zr;
end

    