import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
ps_letters = int(input("How many letters would you like in your password?\n")) 
ps_symbols = int(input(f"How many symbols would you like?\n"))
ps_numbers = int(input(f"How many numbers would you like?\n"))

password=""
for char in range(1,ps_letters+1):
    password+=random.choice(letters)+" "
for symbol in range(1,ps_symbols+1):
    password+=random.choice(symbols)+" "
for number in range(1,ps_numbers+1):
    password+=random.choice(numbers)+" "
for password_str in password:
    password_str=password.split()
hard_password=""
for word in range(1,len(password_str)+1):
    word=random.choice(password_str)
    hard_password+=word
    password_str.remove(word)
print(f"your password is : {hard_password}")

#USING random.suffle() METHOD
# password_list = []

# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))

# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#   password += char

# print(f"Your password is: {password}")