#統計系黃稚元h24124042
n=int(input("Enter an integer:"))
total=0
a=0
b=1
i=2
if n<0:
    print("input again")
elif n==0:
    print(0)
elif n==1 or n==2:
    print(1)
else:
    while i<=n:
        c=a+b
        a=b
        b=c
        i+=1
    print("The {}-th number in Fibonacci sequence is {}".format(n,c))