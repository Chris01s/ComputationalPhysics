from numpy import sin,sqrt


def f(x):
    return sin(sqrt(100*x))*sin(sqrt(100*x))
    
def Adaptive_Simp(f,a,b,N):
    epsilon = 1E-6
    h = abs(b-a)/N
    
    S1 = (f(a) + f(b) + 2*sum([f(a + k*h) for k in range(2,N-1,2)]))/3
    T1 = 2.0*sum([f(a + k*h) for k in range(1,N,2)])/3
    
    I1 = h*(S1 + 2*T1)

    while True:
        N *= 2
        h = abs(b-a)/N
        T2 = 2.0*sum([f(a + k*h) for k in range(1,N,2)])/3
        S2 = S1 + T1
        I2 = h*(S2 + 2*T2)
        if abs(I2 - I1)/15 < epsilon:
            break
        else:
            I1, I2 = I2, 0.0
            S1, S2 = S2, 0.0
            T1, T2 = T2, 0.0

    return I2, N
a = 0.0
b = 1.0
N = 1
print Adaptive_Simp(f,a,b,N)


            
        
        
        
        


