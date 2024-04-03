import random
import string
import csv

special_char = ['_','&','!','?',';','@','^']
special_char = ''.join(special_char)
allowed_char = string.ascii_uppercase + string.digits + string.ascii_lowercase + special_char


def password_generator():
    length = random.randint(20,50)
    full_pass = ''.join(random.SystemRandom().choice(allowed_char) for _ in range(length))
    return full_pass
    
with open('list.csv', 'w', newline='') as file:
    
    writer = csv.writer(file)
    writer.writerow(['passwords'])
    
    iteration_num = range(0, 10)
    
    for i in iteration_num:
        password = password_generator()
        print(password)
        writer.writerow([password])









