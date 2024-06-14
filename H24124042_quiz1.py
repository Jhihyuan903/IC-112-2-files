Richter=float(input("Please input a Richter scale value:"))#Richter value
energy=10**(1.5*Richter+4.8)#calculate energy
Joules=energy
TNT=energy/4.184*(10**9)#calculating how many times of TNT
lunches=energy/2930200#calculating how many times of lunches
print("Richter scale value: {}".format(Richter))
print("Equivalence in Joules:{}".format(energy))
print("Equivalence in tons of TNT:{}".format(TNT))
print("Equivalence in the number of nutritious lunches:{}".format(lunches))