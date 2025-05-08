import string
import random
import method1.my_module as my_module

symbols=['@','#','$','&','!','^','*','~','+']
alphabet_list = list(string.ascii_letters)
value=""
num=int(input("Chose the length of your password between 8 to 16 characters: "))

if num>=8 and num<=16:
    if num%2 ==0:
        for i in range ((num//2)-1):
            value +=random.choice(alphabet_list) + str(random.choice(my_module.numbers))
        value += random.choice(symbols) + random.choice(symbols)
        print(value)
    
    else:
        for i in range ((num-1)//2):
            value +=random.choice(alphabet_list) + str(random.choice(my_module.numbers))
        value += random.choice(symbols)
        print(value)
else:
    print("Invalid")
       