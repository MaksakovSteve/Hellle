def print_person(name,*,age,company):
    print(f"name: {name}, Age: {age}, Company: {company}")
print_person("Tom",age=10,company="Intel")

def print_fullname(firstname,/,secondname,surname):
    print(f"firstname= {firstname}\n,secondname= {secondname}\n,surname ={surname}")

print_fullname("Ivan","Ivanovich","Ivanov")