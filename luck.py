import random as ak
def game():
    a=ak.randint(1,100)
    print(a)
    print("Select your mode:\n1. Easy (7 chances)\n2. Moderate (5 chances)\n3. Difficult (3 chances)")
    ch=int(input("Enter here: "))
    while ch>3 or ch<1:
        ch=int(input("Enter a valid mode: "))
    if ch==1:
        print("Easy")
        limit=7
    elif ch==2:
        print("Moderate")
        limit=5
    else:
        print("Difficult")
        limit=3
    n=int(input("Enter a number in range of 1 to 100: "))
    while n>100 or n<1:
        n=int(input("Invalid input. Re-enter the value: "))
    p=1
    while p<=limit:
        if n==a:
            print(f"Congrats! You have won in {p} attempt(s)!")
            break
        elif n>a:
            print("Your number is greater than the original.")
        else:
            print("Your number is less than the original.")
        if p==limit:
            print("Sorry! You've used all your chances.")
            print(f"The correct number was: {a}")
            break
        n=int(input(f"Attempt {p+1} in {limit} - Try again: "))
        while n>100 or n<1:
            n=int(input("Invalid input. Re-enter the value: "))
        p+=1
while True:
    game()
    z=input("Do you want to play again? (y/n): ").lower()
    if z!="y":
        print("Thanks for playing!")
        break