
def say_hello(): print("Hello")
message=say_hello
message()
def sum(a,b): return a+b
operation=sum
result=operation(1,2)
print(result)

def do_operation(a,b,operation):
    res=operation(a,b)
    print(f"Result = {res}")
def summa(a,b): return a+b
def multipy(a,b): return a*b
do_operation(10,20,multipy)
do_operation(20,2,summa)

from math import sqrt
def dlina(a):
    return sqrt(a)
def perim(a,operation):
    print(operation(a)*4)
perim(100,dlina)














