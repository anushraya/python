num1=int(input("enter 1st num"))
num2=int(input("enter 2nd num"))
total=num1+num2
print("total is" +str(total))


num2=float("44")
num3=int("55")
print(num2+num3)

#two or more input function in one line
name,age=input("enter your name&age").split()
print(name)
print(age)
#or
name,age=input("enter your name&age").split(",")
print(name)
print(age)
