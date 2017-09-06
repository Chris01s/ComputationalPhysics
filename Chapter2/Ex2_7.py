#Ex 2.7


C = 1
n = 0
while C < 1E6:
    C *= (4*n + 2)/float(n + 2)
    n += 1
    print int(C),
    
    
