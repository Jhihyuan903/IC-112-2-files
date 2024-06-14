#統計系黃稚元h24124042
s=str(input("Enter a string:"))
maxlength=0
result=""

for i in range(len(s)):
    l,r=i,i
    while l>=0 and r<len(s) and s[l] == s[r]:
        if maxlength<r-l+1:
            maxlength=r-l+1
            result=s[l:r+1]
        l=l-1
        r=r+1

for i in range(len(s)):
    l,r=i,i+1
    while l>=0 and r<len(s) and s[l] == s[r]:
        if maxlength<r-l+1:
            maxlength=r-l+1
            result=s[l:r+1]
        l=l-1
        r=r+1

print(result)
print("maxlength is "+str(maxlength))