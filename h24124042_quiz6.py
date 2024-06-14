
import random
l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
random.shuffle(l)#打亂 l 裡的排序
goal=l.pop()#隨機取出目標字母
l_input=[goal]#store the input and the target
#判斷輸入字母的位置前後
k=True
while k:
    n=input("Guess the lowercase alphabet:")
    l_input+=[n]
    t=sorted(l_input)
    a=len(l_input)-1#計算猜的次數
    if t.index(n)>t.index(goal):#比較兩字母排序
        print("The alphabet you are looking for is alphabetically lower")
    elif n==goal:
        print("Congratulation! You guessed the alphabet "+goal+"in "+str(a)+"tries")
        k=False
    elif n not in l:
        print("Please enter a lowercase alphabet")
    else:
        print("The alphabet you are looking for is alphabetically higher")
    
#print the guess histogram
#count times
a_d=0
e_h=0
i_l=0
m_p=0
q_t=0
u_x=0
y_z=0
print("Guess histogram")
s=["a","d","e",'h','i','l','m','p','q','t','u','x','y','z']
for i in range(0,len(l_input)):
    l_input[i].append(s)
    t1=s.sorted
    if t1.index("a")<=t1.index(l_input[i])<=t1.index("d"):
        a_d+=1
    elif t1.index("e")<=t1.index(l_input[i])<=t1.index("h"):
        e_h+=1
    elif t1.index("i")<=t1.index(l_input[i])<=t1.index("l"):
        i_l+=1
    elif t1.index("m")<=t1.index(l_input[i])<=t1.index("p"):
        m_p+=1
    elif t1.index("q")<=t1.index(l_input[i])<=t1.index("t"):
        q_t+=1
    elif t1.index("u")<=t1.index(l_input[i])<=t1.index("x"):
        u_x+=1
    else:
        y_z+=1
    s=[]
print("a_d:"+"*"*a_d)
print("e_h:"+"*"*e_h)
print("i_l:"+"*"*i_l)
print("m_p:"+"*"*m_p)
print("q_t:"+"*"*q_t)
print("u_x:"+"*"*u_x)
print("y_z:"+"*"*y_z)