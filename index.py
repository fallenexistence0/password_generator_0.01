import secrets
import string
import csv
import hashlib
special_char = ['_','&','!','?',';','@','^']
special_char = ''.join(special_char)
allowed_char = string.ascii_uppercase + string.digits + string.ascii_lowercase + special_char


def password_generator():
    length = secrets.randbelow(31) + 20
    full_pass = ''.join(secrets.choice(allowed_char) for _ in range(length))
    return full_pass

def hash_password(password) :
    hasher = hashlib.sha256()
    hasher.update(password.encode())
    hashed_password = hasher.hexdigest()
    return hashed_password
    
with open('list.csv', 'w', newline='') as file:
    
    writer = csv.writer(file)
    writer.writerow(['hashed_passwords'])
    
    iteration_num = range(0, 10)
    
    for i in iteration_num:
        password = password_generator()
        hashed_password = hash_password(password)

        print(hashed_password)
        print(password)
        writer.writerow([hashed_password])









