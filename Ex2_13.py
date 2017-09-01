#Ex.2.13

#a)
#with recursion
def Catalan(n):
    if n == 0:
        return 1
    else:
        return Catalan(n-1)*(4*n-2)/(n+1)
    
#without recursion
def Cat_num(n):
    Cat = 1
    for i in range(1,n):
        Cat *= (4*i + 2)/float(i+2)
        print int(Cat)
    
#b)
#with recursion
def g(m,n):
    if n == 0:
        return m
    else:
        return g(n,m%n)
    

##without recursion: illustrates the power of recursion
def gg(m,n):
    #define function to get a value's list of factors
    def divs(a):
        divisors = []
        for i in range(1,a):
            if a%i == 0:
                divisors.append(i)
        return divisors

    #Now define a function to return two unique lists in order of length
    def isSmaller(a,b):
        if len(set(a)) < len(set(b)):
            return set(a),set(b)
        else:
            return set(b),set(a)
    
    #then define a function that compares two lists of factors, list1 & list2
    #and returns a list of factors that are common to both list1 & list2
    def compare(a,b):
        list1, list2 = isSmaller(a,b)
        commonValues = []
        for value in list1:
            if value in list2:
                commonValues.append(value)
        return commonValues

    return max(compare(divs(n),divs(m)))
