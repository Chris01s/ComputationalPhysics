def factorial(n):
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)

print factorial(200) ##returns a long int
print factorial(200.0) #returns an "inf" dtype



