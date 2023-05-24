import random
from art import logo

print(logo)

letters = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', "J", 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '(', '*', '%', '&', '#', ')', '$', '+', '@']

print("** Welcome to Password Generator! **\n")

usr_let = int( input("How many letters do you want?: "))
usr_num = int( input("How many numbers do you want?: "))
usr_sym = int( input("How many symbols do you want?: "))

passcode = []
for letter in range(usr_let):
    passcode.append(random.choice(letters))
for number in range(usr_num):
    passcode.append(random.choice(numbers))
for symbol in range(usr_sym):
    passcode.append(random.choice(symbols))

random.shuffle(passcode)

password = ""
for item in passcode:
    password += item

print(f"\nYour password is:   {password}\n\n")

