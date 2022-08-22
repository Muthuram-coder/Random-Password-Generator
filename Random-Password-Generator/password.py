<<<<<<< HEAD:password.py
from operator import length_hint
import string
import random
password = list(string.ascii_letters + string.digits + "!@#$%^&*")
def password_generator():
    length = int(input("Enter the size of the password you want to create: "))
    
    main = []
    for i in range(length):
        main.append(random.choice(password))
    random.shuffle(main)
    print("".join(main))

password_generator()
=======
from operator import length_hint
import string
import random
password = list(string.ascii_letters + string.digits + "!@#$%^&*")
def password_generator():
    length = int(input("Enter the size of the password you want to create: "))
    random.shuffle(password)
    main = []
    for i in range(length):
        main.append(random.choice(password))
    random.shuffle(main)
    print("".join(main))

password_generator()
>>>>>>> 66f062c14065110a0191cd7636863daa285ed747:Random-Password-Generator/password.py
