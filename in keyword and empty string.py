#IN KEYWORD
alpha=input("enter alphabet")
name=(input("enter your name"))
if alpha in name:
    print("alphabet is present in name")
else:
    print("not present")

#CHECK WHETHER STRING IS EMPTY OR NOT

name=input("enter your name")
if name:
    print(F"your name is{name}")
else:
    print("you didn't type anything")