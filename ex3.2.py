name,age=input("enter your name and age").split()
if (name[0]== 'A' or name[0]=='a') and int(age) >14:
    print("you can play this game")
else:
    print("you cannot play")