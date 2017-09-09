## linear interpolation

def lin_interpolate(f,x,a,b):
    if (x <= a) and (x => b):
        print "interpolated value must be within range specified"
    else:
        return ((b-x)*f(a) + (x-a)*f(b))/(b-a)


        
