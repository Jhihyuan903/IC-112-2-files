print("welcome to the simple calculator program")
k=True
while k:
    n1=float(input("Enter the first number:"))
    n2=float(input("Enter the second number:"))
    a=str(input("Select an arithmetic(+,-,*,/):"))
    while a!="":
        if a=="/":
            if n2==0:
                print("division by zero")
                break
            else:
                print(n1/n2)
        elif a=="-":
            print(n1-n2)
        elif a=="*":
            print(n1*n2)
        else:
            print(n1+n2)
        break
    answer=str(input("Do you want to perform another calculation(yes or no):"))
    if answer=="yes":
        k=True
    else:
        k=False
        print("Good bye")