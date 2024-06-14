#統計系黃稚元h24124042
n=int(input("Input the range number:"))
for i in range(1,n+1):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum=sum+j
    if sum==i:
        print(sum)