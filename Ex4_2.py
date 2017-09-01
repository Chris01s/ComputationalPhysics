from math import sqrt

#a)
def quadratic(a,b,c):
    discriminant = sqrt(b**2 - 4*a*c)
    x_low = (-b - discriminant)/(2*a)
    x_high =(-b + discriminant)/(2*a)
    return x_high, x_low

a, b, c = 0.001, 1000, 0.001

print quadratic(a,b,c)

#b)
def alt_quadratic(a,b,c):
    discriminant = sqrt(b**2 - 4*a*c)
    x_high = 2*c/(-b - discriminant)
    x_low = 2*c/(-b + discriminant)
    return x_high, x_low

print alt_quadratic(a,b,c)
