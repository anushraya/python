

# def func():
#     x=7
#     return x
# print(func())


# x=5  #global variable
# def func():
#     x=2 #local variable
#     return x
# print(func())
# print(x)


#changing value of global variable x
# x=5
# def func():
#     global x
#     x=7   #local variable
#     return x
# print(func())
# print(x)


# x=5
# def func():
#     global x
#     x=7   #local variable
#     return x
# print(x)
# print(func())

x=5
def func():
    global x
    x=7   #local variable
    return x
print(x)
print(func())
print(x)