function [a0,a1,a2,a3,a4,a5,a6,b0,b1,b2,b3,b4,b5]=solveMF(xs,zs,...
            xh,zh,xf,zf,ts,th,tf)
      A=[1,ts,ts^2,ts^3,ts^4,ts^5,ts^6;
         1,th,th^2,th^3,th^4,th^5,th^6;
         1,tf,tf^2,tf^3,tf^4,tf^5,tf^6;
         0,1,2*ts,3*ts^2,4*ts^3,5*ts^4,6*ts^5;
         0,0,2,6*ts,12*ts^2,20*ts^3,30*ts^4;
         0,1,2*tf,3*tf^2,4*tf^3,5*tf^4,6*tf^5;
         0,0,2,6*tf,12*tf^2,20*tf^3,30*tf^4;];
      B=[1,ts,ts^2,ts^3,ts^4,ts^5;
         1,th,th^2,th^3,th^4,th^5;
         1,tf,tf^2,tf^3,tf^4,tf^5;
         0,1,2*ts,3*ts^2,4*ts^3,5*ts^4;
         0,1,2*th,3*th^2,4*th^3,5*th^4;
         0,1,2*tf,3*tf^2,4*tf^3,5*tf^4;];
       a=[xs;xh;xf;0;0;0;0];
       b=[zs;zh;zf;0;0;0];
       asolve = mldivide(A,a);
       bsolve = mldivide(B,b);
       a0=asolve(1);a1=asolve(2);a2=asolve(3);a3=asolve(4);
       a4=asolve(5);a5=asolve(6);a6=asolve(7);
       b0=bsolve(1);b1=bsolve(2);b2=bsolve(3);
       b3=bsolve(4);b4=bsolve(5);b5=bsolve(6);
end