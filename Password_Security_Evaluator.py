print("Welcome to the Password Security Checker")
common_passwords= ["password", "123456", "123456789", "qwerty", "abc123","password1", "111111", "123123", "admin", "letmein","welcome", "monkey", "login", "princess", "qwerty123"]
password=input("Enter a password: ")

lenght= len(password)
print(f"Lenght: {lenght}")
min_lenght = 8
if lenght >=min_lenght:
    lenght_ok = True
else:
    lenght_ok = False

has_uppercase = False
for char in password:
    if char.isupper():
        has_uppercase = True
        break

if has_uppercase:
    print("Uppercase: YES")
else:
    print("Uppercase: NO")

has_lowercase = False
for char in password:
    if char.islower():
        has_lowercase = True
        break

if has_lowercase:
    print("Lowercase: YES")
else:
    print("Lowercase: NO")

has_numbers = False
for char in password:
    if char.isdigit():
        has_number = True
        break

if has_numbers:
    print("Numbers: YES")
else:
    print("Numbers: NO")

special_characters = '!@#$%^&*()_+-=[]{}|;:,.<>?/'
has_special_characters = False
for char in password:
    if char in special_characters:
        has_special_characters = True
        break

if has_special_characters:
    print("Special Characters: YES")
else:
    print("Special characters: NO")

is_common = False
password_lower = password.lower()
for common in common_passwords:
    if password_lower == common:
        is_common = True
        break

if is_common:
    print("Common password: YES")
else:
    print("Common password: NO")

has_repeated = False
for i in range(len(password)-2):
    if password[i] == password[i+1] == password[i+2]:
        has_repeated= True
        break

if has_repeated:
    print("Repeated characters: YES")
else:
    print("Repeated characters: NO")

score = 0
if lenght >=8:
    score += 1
if lenght >=12:
    score +=1
if has_uppercase:
    score +=1
if has_lowercase:
    score +=1
if has_numbers:
    score +=1
if has_special_characters:
    score +=1

if is_common:
    score = 0
if has_repeated:
    score -=1

if score <=2:
    strenght = "WEAK"
elif score <=4:
    strenght = "MEDIUM"
else:
    strenght = "STRONG"
print(f"Strenght: {strenght}")
print()
