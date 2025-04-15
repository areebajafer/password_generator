import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0','1','2','3','4','5','6','7','8','9']

print("Welcome to the Password generator")

n_letters = input("how many letter would u like in ur password?\n")
n_symbols = input(f"how many symbols would u like in ur password\n")
n_numbers = input(f"how many numbers would u like in ur password\n")

if not n_letters.isdigit() or not n_symbols.isdigit() or not n_numbers.isdigit():
    print("enter a valid number please")
else:
    password =  []

for i in range(0,int(n_letters)):
    random_letter=random.randint(0,51)
    password.append(letters[random_letter])

for i in range(0,int(n_symbols)):
    random_symbol=random.randint(0,8)
    password.append(symbols[random_symbol])

for i in range(0,int(n_numbers)):
    random_number=random.randint(0,9)
    password.append(numbers[random_number])

random.shuffle(password)
print(f"here is ur password: {''.join(password)}")

if len(password) <= 6:
    print("ur password is weak, try again!")
elif len(password) == 7:
    print("ur password is medium, try a stronger password!")
else:
   print("ur password is strong!")