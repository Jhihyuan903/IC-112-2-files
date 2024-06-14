#統計系 黃稚元 H24124042
board=[[0,1,2,3,4,5,6],[0,1,2,3,4,5]]#col,row
listk=[" "," "," "," "," "," "," "]#store the symbol position input by the players
#create a gameboard
i=1
print("+"+"---+"*7)
while i<=int(len(board[1])):
    print("|"+"   |"*7)
    print("+"+"---+"*7)
    i+=1
for i in range(int(len(board[0]))):
    print("  {}".format(i),end=" ")
print()
#let the X player and the O player input the symbol into the column they choosed 
#make sure the column is not full of symbols
D=True
while D:
    x=int(input("Player X>>"))
    listk[x]="X"
    print(listk)
    
    o=int(input("Player O>>"))
    listk[o]="O"
    print(listk)
    