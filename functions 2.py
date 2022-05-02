#function to print last character
def last_char(name):
    return name[-1]
name=input("enter name")
print(last_char(name))


#function to define odd_even
def odd_even(num):
    if num%2==0:
        return"even"
    return"odd"
print(odd_even(4))

#fuction defining even number
def is_even(num):
    if num%2==0:
        return"true"
print(is_even(10))

#
def song():
    return"happy birthday"
print(song())