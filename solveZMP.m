function [x_zmp,y_zmp] = solveZMP(x0,y0,z0,x0b,y0b,z0b,x0bb,y0bb,z0bb,...
                                  x1,y1,z1,x1b,y1b,z1b,x1bb,y1bb,z1bb,...
                                  x2,y2,z2,x2b,y2b,z2b,x2bb,y2bb,z2bb,...
                                  x3,y3,z3,x3b,y3b,z3b,x3bb,y3bb,z3bb,...
                                  x4,y4,z4,x4b,y4b,z4b,x4bb,y4bb,z4bb,...
                                  x5,y5,z5,x5b,y5b,z5b,x5bb,y5bb,z5bb,...
                                  x6,y6,z6,x6b,y6b,z6b,x6bb,y6bb,z6bb,...
                                  m0,m1,m2,m3,m4,m5,m6,g,N,tf,ts)
    tsample=(tf-ts)/N;
    ax0=(x0+x0bb-2*x0b)/(tsample^2);
    ax1=(x1+x1bb-2*x1b)/(tsample^2);
    ax2=(x2+x2bb-2*x2b)/(tsample^2);
    ax3=(x3+x3bb-2*x3b)/(tsample^2);
    ax4=(x4+x4bb-2*x4b)/(tsample^2);
    ax5=(x5+x5bb-2*x5b)/(tsample^2);
    ax6=(x6+x6bb-2*x6b)/(tsample^2);
    ay0=(y0+y0bb-2*y0b)/(tsample^2);
    ay1=(y1+y1bb-2*y1b)/(tsample^2);
    ay2=(y2+y2bb-2*y2b)/(tsample^2);
    ay3=(y3+y3bb-2*y3b)/(tsample^2);
    ay4=(y4+y4bb-2*y4b)/(tsample^2);
    ay5=(y5+y5bb-2*y5b)/(tsample^2);
    ay6=(y6+y6bb-2*y6b)/(tsample^2);
    az0=(z0+z0bb-2*z0b)/(tsample^2);
    az1=(z1+z1bb-2*z1b)/(tsample^2);
    az2=(z2+z2bb-2*z2b)/(tsample^2);
    az3=(z3+z3bb-2*z3b)/(tsample^2);
    az4=(z4+z4bb-2*z4b)/(tsample^2);
    az5=(z5+z5bb-2*z5b)/(tsample^2);
    az6=(z6+z6bb-2*z6b)/(tsample^2);
    
    x_zmp=(m0*(az0*x0+g*x0-ax0*z0)+m1*(az1*x1+g*x1-ax1*z1)+...
           m2*(az2*x2+g*x2-ax2*z2)+m3*(az3*x3+g*x3-ax3*z3)+...
           m4*(az4*x4+g*x4-ax4*z4)+m5*(az5*x5+g*x5-ax5*z5)+...
           m6*(az6*x6+g*x6-ax6*z6))/(m0*(az0+g)+m1*(az1+g)+...
           m2*(az2+g)+m3*(az3+g)+m4*(az4+g)+m5*(az5+g)+...
           m6*(az6+g));
    y_zmp=(m0*(az0*y0+g*y0-ay0*z0)+m1*(az1*y1+g*y1-ay1*z1)+...
           m2*(az2*y2+g*y2-ay2*z2)+m3*(az3*y3+g*y3-ay3*z3)+...
           m4*(az4*y4+g*y4-ay4*z4)+m5*(az5*y5+g*y5-ay5*z5)+...
           m6*(az6*y6+g*y6-ay6*z6))/(m0*(az0+g)+m1*(az1+g)+...
           m2*(az2+g)+m3*(az3+g)+m4*(az4+g)+m5*(az5+g)+...
           m6*(az6+g));
end