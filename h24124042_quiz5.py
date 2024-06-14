n=int(input("Enter the size of grid:"))#the size eof grid


for i  in range(1,n+1):#印出grid
    print("_ "*n, end="")
    print()
k=True
while k:
    s=input("Enter the cell coordinate to edit:")#coordinate
    s=s.split(",")#str -> list
    value=str(input("Enter the new value for the cell:"))#value
    a=int(s[0])#coordinate of row
    b=int(s[1])#coordinate of column
    if s=="done":#結束程式
        k=False
    else:
        l=[]
        for i  in range(1,n+1):
           
            l=l+["_ "]
            print(l)
        