#統計系 黃稚元 H24124042
n=int(input("Input the total number of students(n>0):"))
l=[]
#initializing two variables
i=1
j=0

#creating a list of students and store the characters in the list "l"
while i<=n:
    l+=[i]
    i+=1
#keep removing the students ID who reports the number 3 until there is only one left
while len(l)>1:
    j=(j+2)%len(l)#moving to the next one who reports 3
    l.pop(j)#remove the ID who reports 3

print("The last ID is "+str(l[0]))#output the outcome
        






















"""
while i <=n:
   l +=[i]
   i+=1
   while j<= len(l):
       if l.append(j%3)==0:
           l=l[0:j-1]+l[j+1:]
       j+=1
print(l)
"""