#Ex 2.11

from pylab import plot, show
#a)
def binomial(n,k):
    def fact(a):
        if a <= 1:
            return 1
        else:
            return a*fact(a-1)
    return fact(n)/(fact(k)*fact(n-k))

#b)
def PascalTriangle(n,k,no_of_lines):
    for n in range(no_of_lines):
        print "\n"
        for k in range(n+1):
            print binomial(n,k),

#c)
#i)
n = 100.0
k = 60.0
print "Probability that a coin tossed %d \
times comes up heads %d times is %f"%(n,k,binomial(n,k)/2**n)
#ii)
get60Plus = [binomial(n,k)/2**n for k in range(60,101)]
pTotal = sum(get60Plus)
print "Probability that a coin tossed %d \
times comes up heads %d times is %f"%(n,k,pTotal)
plot(get60Plus)
show()
