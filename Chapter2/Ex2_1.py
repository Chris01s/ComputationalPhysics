#Ex 2.1

height = float(input("enter height from which the ball will be dropped: "))#metres
#use simple kinematics equations
gravity = 9.81 #m/s
#distance = height = 1/2 * g * t^2: rearrange for t and we get the time taken, under
#constant acceleration, for the ball to hit the ground
time = sqrt(2*height/gravity)
print time