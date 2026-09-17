import string
import secrets


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    character_sets = []

    if use_upper:
        character_sets.append(string.ascii_uppercase)

    if use_lower:
        character_sets.append(string.ascii_lowercase)

    if use_digits:
        character_sets.append(string.digits)

    if use_symbols:
        character_sets.append(string.punctuation)

    if not character_sets:
        return None

    if length < len(character_sets):
        return None

    # Guarantee at least one character from every selected category
    password = [
        secrets.choice(characters)
        for characters in character_sets
    ]

    # Combine all selected character sets
    all_characters = ''.join(character_sets)

    # Fill remaining positions
    for _ in range(length - len(password)):
        password.append(secrets.choice(all_characters))

    # Securely shuffle the password
    for i in range(len(password) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password[i], password[j] = password[j], password[i]

    return ''.join(password)


def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(not char.isalnum() for char in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def get_yes_no(message):
    while True:
        answer = input(message).strip().lower()

        if answer in ("y", "yes"):
            return True

        if answer in ("n", "no"):
            return False

        print("Please enter Y or N.")


def generate_password_menu():
    while True:
        try:
            length = int(input("\nEnter password length: "))

            if length < 4:
                print("Password length must be at least 4.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    use_upper = get_yes_no("Include uppercase letters? (Y/N): ")
    use_lower = get_yes_no("Include lowercase letters? (Y/N): ")
    use_digits = get_yes_no("Include numbers? (Y/N): ")
    use_symbols = get_yes_no("Include symbols? (Y/N): ")

    selected_categories = sum([
        use_upper,
        use_lower,
        use_digits,
        use_symbols
    ])

    if selected_categories == 0:
        print("You must select at least one character type.")
        return

    if length < selected_categories:
        print(
            f"Length must be at least {selected_categories} "
            "for the selected character types."
        )
        return

    password = generate_password(
        length,
        use_upper,
        use_lower,
        use_digits,
        use_symbols
    )

    print("\nGenerated Password :", password)
    print("Password Strength  :", check_strength(password))


def main():
    while True:
        print("\n========== PASSWORD MANAGER ==========")
        print("1. Generate Password")
        print("2. Check Password Strength")
        print("3. Exit")
        print("======================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            generate_password_menu()

        elif choice == "2":
            password = input("Enter password: ")
            print("Password Strength:", check_strength(password))

        elif choice == "3":
            print("Program terminated.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
