import random
import string

def gen_password(length: int) -> str:
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )
    return ''.join(random.choice(characters) for _ in range(length))

def cp(s: str) -> bool:
    isu = False
    isd = False
    iss = False
    for i in s:
        if i.isupper():
            isu = True

        if i.isdigit():
            isd = True

        if not i.isspace() and not i.isalnum():
            iss = True
    return isu and isd and iss

while True:
    length = int(input("Enter Password Length: "))
    while length < 8:
        print("Password length must be at least 8.")
        length = int(input("Please enter again: "))

    while True:
        password = gen_password(length)

        if cp(password):
            print("Generated Password:", password)
            print("Password is valid.")
            break

    break
