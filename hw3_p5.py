
#統計系黃稚元h24124042
a=int(input("Enter the number of layers(2 to 5):"))#the number of layers
b=int(input("Enter the side length of the top layer (2 to 6):"))#top_length 
c=int(input("Enter the growth of each layers(1 to 5):"))#growth 
d=int(input("Enter the width of the trunk (3 to 9, odd number):"))#trunk_width 
e=int(input("Enter the height of the trunk (4 to 10):"))#trunk_height 
space=b+c*(a-1)-1
print(" "*(space)+"#")
for i in range (1,a+1):
    if i==1 and b==2:
        print(" "*(space-1)+"#"*3)
    else:
        for j in range(1,b):
            if j!=b-1:    
                print(" "*(space-j)+"#"+"@"*(2*j-1)+"#")
            else:
                print(" "*(space-j)+"#"+"#"*(2*j-1)+"#")
    b=b+c
for k in range(1,e+1):
        print(" "*((space-d//2))+"|"*d,sep="")
