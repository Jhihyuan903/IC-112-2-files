s=str(input("Enter a sequence of integers separated by whitespace:"))#s is a string
s=s.split(" ")#transform s to a list
LICS=[]#store the outcome of Longest Increasing Continuous Sequence
for i in range(0,len(s)):#逐一檢查s中的各個元素，並以各個元素為開頭
    k=[]#initialize the list k
    k.append(int(s[i]))#add the i-th element in the list s into list k
    for j in range(i,len(s)):# repeatedly operate the loop for len(s) times
        if int(s[j])>int(k[-1]):#determine whether the value is greater than the next one
            k.append(int(s[j]))
            
    if len(LICS)<len(k):#determine whether the following one is longer than the previous one 
        LICS=k#adjust the length of LICS
    
print("Length:",len(LICS))
print("LICS:",LICS)