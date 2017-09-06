from math import sqrt

#initialise the set of primes
primes = [2]

#iterate through values 3 to 10,000
for n in range(3,10000):
    #flag for non prime values: set to zero
    foundNonPrime = 0

    #check each value in the current list of
    #primes, up to and including sqrt(n), if n is divisble by them
    #if so, flag it and break out of the loop. If not found, flag
    #stays at zero, and n is added to update the list of primes
    for p in primes:
        if (n%p) == 0:
            foundNonPrime = 1
            break
        elif p > sqrt(n):
            break
    if foundNonPrime == 1:
        continue
    else:
        primes.append(n)

#print results
print primes
