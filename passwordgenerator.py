import random
import string

length = int(input("Input password length: "))
characterList = string.ascii_letters + string.digits + string.punctuation

password = []

for i in range(length):
    randomchar = random.choice(characterList)
    password.append(randomchar)
    
print("Your password is: " + "".join(password))