F=float(input("please input the force:"))#input the value of F 
G=6.67*(10**-11)#gravity constant
m1=float(input("please input the mass:"))#input the mass of object 1
d=float(input("please input the distance:"))#input the value of distance
c=299792458#the speed of light
m2=F*(d**2)/(G*m1)#calculating the mass of object 2
print("the mass of m2 is {}".format(m2))#print outcome of m2
E=m2*(c**2)#the energy formula
print("The energy of m2 is {}".format(E))
