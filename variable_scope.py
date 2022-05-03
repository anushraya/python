

# def func():
#     x=7
#     return x
# print(func())


x=5  #global variable
def func():
    x=2 #local variable
    return x
print(func())
print(x)
