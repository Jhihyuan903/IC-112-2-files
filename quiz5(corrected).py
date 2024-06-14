n=int(input("Enter the size of grid:"))
matrix=[["_" for j in range(0,n)]for i in range(n)]
print(matrix)
k=True
while k:
    coordinate=input("Enter the coordinate:")
    if coordinate=="done":
        break
    row,col=coordinate.split(",")
    row,col=int(row),int(col)
    newvalue=input("Enter the new value:")
    matrix[row][col]=newvalue
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end=" ")
        print()