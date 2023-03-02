#myfile=open("hello.txt","w")
#myfile.write("HelloWorld")
#myfile.close()
Filename="message.txt"
messages=list()
for i in range(4):
    message1=input("Enter "+str(i+1)+" : ")
    messages.append(message1+"\n")
with open(Filename,"a") as file:
    for message1 in messages:
        file.write(message1)
#print(messages)