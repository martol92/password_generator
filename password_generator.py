import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


sizeletter = len(letters)
sizenum = len(numbers)
sizesym = len(symbols)

password_char_list = []

for i in range(1, nr_letters+1):
    random_char_index = random.randint(0, sizeletter-1)
    password_char_list.append(letters[random_char_index])
for j in range(1, nr_symbols+1):
    random_char_index = random.randint(0, sizesym-1)
    password_char_list.append(symbols[random_char_index])
for k in range(1, nr_numbers+1):
    random_char_index = random.randint(0, sizenum-1)
    password_char_list.append(numbers[random_char_index])

password = "".join(password_char_list)
print("This is password", password)
pass_shuffled = random.shuffle(password_char_list)
print("This is password after shuffle", "".join(password_char_list))






