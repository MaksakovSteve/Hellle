def person(name="Tom",age=18,*children):
    print(f"{name}, {age}",end="\n")
    for i in children:
        print(i,end=" ")
person()
person(age=10)
person("Ivan",22,"Bob","Tom")