def summa(a,b):
    return a+b
def multipy(a,b):
    return a*b
def subtract(a,b):
    return a-b

def select_op(enter):
    if enter=="+":
        return summa#summa(a,b)
    elif enter=="-":
        return subtract
    elif enter=="*":
        return multipy
    else:
        return "Error"

x1=int(input("Enter 1st number"))
znak=input("Enter znak")
x2=int(input("Enter 2st number"))
operation=select_op(znak)#
print(operation(x1,x2))
print(select_op(znak)(x1,x2))