#統計系黃稚元h24124042
n=int(input("The number of requested element in Fibonacci:"))
s1=str(input("The first string for palindromic detection:"))
s2=str(input("The second string for palindromic detection:"))
s3=str(input("The plaintext to be encrypted:"))

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
k=c

#determine the value of k
i=0
maxlength1=0
result1=""
for i in range(len(s1)):
    l,r=i,i
    while l>=0 and r<len(s1) and s1[l] == s1[r]:
        if maxlength1<r-l+1:
            maxlength1=r-l+1
            result1=s1[l:r+1]
        l=l-1
        r=r+1

for i in range(len(s1)):
    l,r=i,i+1
    while l>=0 and r<len(s1) and s1[l] == s1[r]:
        if maxlength1<r-l+1:
            maxlength1=r-l+1
            result1=s1[l:r+1]
        l=l-1
        r=r+1


a=maxlength1

i=0
maxlength2=0
result2=""
for i in range(len(s2)):
    l,r=i,i
    while l>=0 and r<len(s2) and s2[l] == s2[r]:
        if maxlength2<r-l+1:
            maxlength2=r-l+1
            result2=s2[l:r+1]
        l=l-1
        r=r+1

for i in range(len(s2)):
    l,r=i,i+1
    while l>=0 and r<len(s2) and s2[l] == s2[r]:
        if maxlength2<r-l+1:
            maxlength2=r-l+1
            result2=s2[l:r+1]
        l=l-1
        r=r+1
b=maxlength2
print("The {}-th number in Fibonacci sequence is {}".format(n,c))
print("Longest palindorme substring within first string is: {}".format(result1))
print("length is "+str(maxlength1))
print("Longest palindorme substring within second string is: {}".format(result2))
print("length is "+str(maxlength2))
w=""
for i in range(len(s3)):
    s=ord(s3[i])
    y1=s+k
    y2=a*y1+b
    if y2>90:
        y2=(y2-65)%26+65
        w+=chr(y2)
print("The encrypted text is:"+ w)
