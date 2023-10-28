import string
import random

lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbol = string.punctuation
number = string.digits

try:
    passlen = int(input("Enter Your Password Length:\n"))

    passlist= []
    passlist.extend(list(lower))
    passlist.extend(list(upper))
    passlist.extend(list(symbol))
    passlist.extend(list(number))

    password = "".join(random.sample(passlist,passlen))
    print("Your Password is:\n ", password)

except ValueError:
    print("\nInvalid Input!")
    print("Please Enter an Integer Number for Password Length\n")