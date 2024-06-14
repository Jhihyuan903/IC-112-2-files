matrix1=[]#store the result
matrix2=[]#manifest the result
def create_matrix(matrix):
    for i in range(0,9):
        temp_row=[]
        for j in range(0,9):
            temp_row.append(" ")
        matrix.append(temp_row)
    return matrix
create_matrix(matrix1)
create_matrix(matrix2)
def store_game():
    col_order=['a','b','c','d','e','f','g','h','i']
    row_separator="  "+"+---"*9+"+"
    print("    ",end="")
    for i in range(0,9):
        print(col_order[i],end="   ")
    print()
    for i in range(0,9):
        print(row_separator)
        print(i+1,"|",end="")
        for j in range(0,9):
            print(" ",matrix2[i][j],end="")
            print("|",end="")
        print()
    print(row_separator)
#create a gamebord
store_game()
def check_mines(n):
    dic={"a":0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8}
    mines=[]
    if len(n)==2:
        #檢查那格是否為地雷
        if matrix1[int(n[1])-1][dic.get(n[0])]=="X":
            print("bomb")
            return "X"
        #檢查右邊
        if matrix1[int(n[1])-1][dic.get(n[0])+1]=="X":
            mines.append("x")
        #檢查右上
        if matrix1[int(n[1])-2][dic.get(n[0])+1]=="X":
            mines.append("x")
        #檢查右下
        if matrix1[int(n[1])][dic.get(n[0])+1]=="X":
            mines.append("x")
        #檢查左邊
        if matrix1[int(n[1])-1][dic.get(n[0])-1]=="X":
            mines.append("x")
        #檢查左上
        if matrix1[int(n[1])-2][dic.get(n[0])-1]=="X":
            mines.append("x")
        #檢查左下
        if matrix1[int(n[1])][dic.get(n[0])-1]=="X":
            mines.append("x")
        #檢查上面
        if matrix1[int(n[1])-2][dic.get(n[0])]=="X":
            mines.append("x")
        #檢查下面
        if matrix1[int(n[1])][dic.get(n[0])]=="X":
            mines.append("x")
        return len(mines)
    
dic={"a":1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9}
import random
#randomly assign mines
for i in range(0,10):
    row=random.randint(0, 8)
    col=random.randint(0, 8)
    matrix1[row][col]="X"
while True:
    n=input("Enter the cell:")
    if len(n)==2:
        matrix2[int(n[1])-1][dic.get(n[0])-1]=check_mines(n)
    store_game()
    if matrix2[int(n[1])-1][dic.get(n[0])-1]=="X":
        break
    elif matrix2[int(n[1])-1][dic.get(n[0])-1]==0:
        
    