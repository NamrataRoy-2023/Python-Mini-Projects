import random
import string
length=int(input("Enter the length of password : "))
char=string.ascii_letters
num = string.digits
special_char = string.punctuation

pass_library=char+num+special_char
password=""
for i in range (length):
    password += random.choice(pass_library)

print("Your password is : ",password)
