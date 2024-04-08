import secrets
import string
import csv
import hashlib
special_char = ['_','&','!','?',';','@','^']
special_char = ''.join(special_char)

# Loop that dictates the type of password to be generated.
while True:
    x = int(input("Would you like to include special characters? (0, 1):"))
    if x == 0:
        allowed_char = string.ascii_uppercase + string.digits + string.ascii_lowercase
        break
    elif x == 1:
        allowed_char = string.ascii_uppercase + string.digits + string.ascii_lowercase + special_char
        break
    else:
        print("Invalid entry please try again.")

# Loop that enforces a minimum password lenght
while True:
    password_lenght = int(input("Enter the number of characters in the password (this includes letters and symbols): "))
    if password_lenght < 10:
        print("The minimum password lenght is 10, please enter a valid entry")
    elif password_lenght >= 10:
        break
    # This line is useless as entering anything other than an int in the password_lenght variable will end the script and give an error.
    else:
        print("Error invalid entry: Please enter a valid number.")

# Functions that generates password
def password_generator():
    length = secrets.randbelow(10) + password_lenght
    full_pass = ''.join(secrets.choice(allowed_char) for _ in range(length))
    return full_pass
# Function that hashes the password
def hash_password(password) :
    hasher = hashlib.sha256()
    hasher.update(password.encode())
    hashed_password = hasher.hexdigest()
    return hashed_password
# Password is written to csv.
with open('list.csv', 'w', newline='') as file:
    
    writer = csv.writer(file)
    writer.writerow(['hashed_passwords'])
     
    password = password_generator()
    hashed_password = hash_password(password)
    print('hashed password is: {} '.format(hashed_password))
    # print('unencrypted password is: {} '.format(password))
    writer.writerow([hashed_password])









