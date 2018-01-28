from random import randrange

#a
rollone = randrange(1,7)
rolltwo = randrange(1,7)

#b
N = 1E6
count = 0

for i in range(int(N)):
    #roll the two dice
    rollone = randrange(1,7)
    rolltwo = randrange(1,7)

    #count if double six
    if (rollone,rolltwo) == (6,6):
        count += 1

print count/N

        
        
        
    
