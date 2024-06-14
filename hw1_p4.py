h=float(input("please input the initial height of ball 1:"))#the height of first ball
m1=float(input("please input the mass of m1:"))#the mass of first ball
m2=float(input("please input the mass of m2:"))#the mass of second ball
g=9.8#gravational accerleration constant
v1=(2*g*h)**(1/2)#the velocity of first ball after slide 
v2=((m1/m2)**(0.5))*v1#the velocity of second ball after collision
print("The velocity of the 1st ball after slide:{} m/s".format(v1))
print("The velocity of the 2nd ball after collision:{} m/s".format(v2))