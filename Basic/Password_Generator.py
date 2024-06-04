#  A Python program for generating passwords using various conditions

import random
import string

def generate_password(min_len, numbers=True, special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits   # appending numbers to the pass
    if special_chars:
        characters += special  # appending special_chars to the pass       
    
    pwd = ""
    has_numbers = False     
    has_special = False

    while len(pwd) < min_len or (numbers and not has_numbers) or (special_chars and not has_special):
        new_char = random.choice(characters)    # choose from characters
        pwd += new_char

        if new_char in digits:      # checking if digit is present
            has_numbers = True
        elif new_char in special:   # checking if special_char is present
            has_special = True

    return pwd

min_length = int(input("Enter the minimum length for your password: "))
has_num = input("Do you want numbers in your password (y/n)? ").lower() == "y"
has_spec = input("Do you want special characters in your password (y/n)? ").lower() == "y"
pwd = generate_password(min_length, has_num, has_spec)
print(f"The password is: {pwd}\n")
