import math
import numpy as np
def integrate(F,x,y,xStop,h,tol=1.0e-6):
    a1 = 0.2; a2 = 0.3; a3 = 0.8; a4 = 8/9.0; a5 = 1.0
    a6 = 1.0

    c0 = 35/384.0; c2 = 500/1113.0; c3 = 125/192.0
    c4 = -2187/6784.0; c5 = 11/84.0

    d0 = 5179/57600.0; d2 = 7571/16695.0; d3 = 393/640.0
    d4 = -92097/339200.0; d5 = 187/2100.0; d6 = 1/40.0

    b10 = 0.2
    
    b20 = 0.075; b21 = 0.225
    
    b30 = 44/45.0; b31 = -56/15.0; b32 = 32/9.0
    
    b40 = 19372/6561.0; b41 = -25360/2187.0; b42 = 64448/6561.0
    b43 = -212/729.0
    
    b50 = 9017/3168.0; b51 =-355.0/33.0; b52 = 46732/5247.0
    b53 = 49/176.0; b54 = -5103/18656.0
    
    b60 = 35/384.0; b62 = 500/1113.0; b63 = 125/192.0;
    b64 = -2187/6784.0; b65 = 11/84.0
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    stopper = 0 # Integration stopper(0 = off, 1 = on)
    k0 = h*F(x,y)
    for i in range(500):
        k1 = h*F(x + a1*h, y + b10*k0)
        k2 = h*F(x + a2*h, y + b20*k0 + b21*k1)
        k3 = h*F(x + a3*h, y + b30*k0 + b31*k1 + b32*k2)
        k4 = h*F(x + a4*h, y + b40*k0 + b41*k1 + b42*k2 + b43*k3)
        k5 = h*F(x + a5*h, y + b50*k0 + b51*k1 + b52*k2 + b53*k3 + b54*k4)
        k6 = h*F(x + a6*h, y + b60*k0 + b62*k2 + b63*k3 + b64*k4 + b65*k5)
        dy = c0*k0 + c2*k2 + c3*k3 + c4*k4 + c5*k5
        E = (c0 - d0)*k0 + (c2 - d2)*k2 + (c3 - d3)*k3 \
        + (c4 - d4)*k4 + (c5 - d5)*k5 - d6*k6
        e = math.sqrt(np.sum(E**2.0)/len(y))
        print e
        hNext = 0.9*h*(tol/e)**0.2
        # Accept integration step if error e is within tolerance
        if e <= tol:
            y = y + dy
            x = x + h
            X.append(x)
            Y.append(y)
            if stopper == 1: break # Reached end of x-range
            if abs(hNext) > 10.0*abs(h): hNext = 10.0*h
            # Check if next step is the last one; if so, adjust h
            if (h > 0.0) == ((x + hNext) >= xStop):
                hNext = xStop - x
                stopper = 1
            k0 = k6*hNext/h
        else:
            if abs(hNext) < 0.1*abs(h): hNext = 0.1*h
            k0 = k0*hNext/h
        h = hNext
    return np.array(X),np.array(Y)

