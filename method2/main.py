import string
import random


symbols={'@','#','$','&','!','^','*','~','+'}
alphabet_list = list(string.ascii_letters)
numbers = set(list(range(1, 10)))
data=symbols.union(alphabet_list,numbers)


value=""
num=int(input("Chose the length of your password between 8 to 16 characters: "))

if num>=8 and num<=16:
    for i in range (num):
        value += str(random.choice(list(data)))
    print("You password is: ",value)
else:
    print("Invalid")