#統計系黃稚元h24124042
y=int(input("Please input the year:"))#year

m=int(input("Please input the month:"))#month
d=1#day
if m==(1 or 3 or 5 or 7 or 8 or 10 or 12):
    days=31
elif m==2 :
    if y%4==0:
        days=29
    else:
        days=28
    if y%100==0 and y%400 !=0:
        days=28
else:
    days=30
if m==1:
    m=13
    y=y-1
if m==2:
    m=14
    y=y-1
c=(y//100)#century
y=y%100

space=(y+int(y/4)+int(c/4)-2*c+int(26*(m+1)/10)+d-1)%7
print("Sun Mon Tue Wed Thu Fri Sat")
print("    "*(space)+"01 ", end=" ")
i=2
while i<=days:
    space=space+1
    if space==7:
        print("",end="\n")
        space=0
    print(str(i).zfill(2)+" ",end=" ")
    i=i+1