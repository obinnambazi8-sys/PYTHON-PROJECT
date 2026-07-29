import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
n_of_letters = int(input("How many letters would you like in your password? "))
n_of_symbols = int(input("How many symbols would you like? "))
n_of_numbers = int(input("How many numbers would you like? "))

password = []
for i in range(n_of_letters):
     l = random.choice(letters)
     password.append(l)

for i in range(n_of_numbers):
     n = random.choice(numbers)
     password.append(n)

for i in range(n_of_symbols):
     s = random.choice(symbols)
     password.append(s)

random.shuffle(password)
final_password = "".join(password)

print(f"your password is: {final_password}")

f = open('password.txt','w')    

