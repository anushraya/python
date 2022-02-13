winning_number="20"
x=input("guess any number between 1-50 ")
if x==winning_number:
    print("you won")
elif x<winning_number:
    print("you had entered a number lower than winning number")
else:
    print("you had entered a number greater than winning number")