name='abc'
age=19
if name=='abc' and age==19:
    print("true")
else:
    print("false")


name='abc'
age=19
if name=='abc' and age==17:
    print("true")
else:
    print("false")

name='abc'
age=19
if name=='abc' or age==18:
    print("true")
else:
    print("false")

name='abc'
age=19
if name=='abcd' and age==17:
    print("true")
else:
    print("false")

#if...elif...else statement
age=int(input("please enter your age"))
if 0<age<=3:
    print("ticket prize=free")
elif 3<age<=10:
    print("ticket prize=150")
elif 10<age<=60:
    print("ticket prize=250")
else:
    print("ticket prize=200")