
print("Hello Mr/Ms")
name = input("Please enter your name")


age = input("please enter your age")

address = input("please enter your address")

if name.isdigit() == False and age.isdigit() == True and len(name)>0 and len(age)>0 and len(address)>0:
    print("Hello Mr/Ms", {name}, "age", {age}, "located in", {address}, "thanks for being in our community,Enjoy")
else:
    print("Error")




