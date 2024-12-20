from secrets import choice

def generate_passwords():
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'

    chars = ''
    how_much_passwords = int(input("How many passwords do you need? "))
    length = int(input("What length should each password be? "))

    digits_inside = input("Do you need digits? (Yes - y, No - n): ")
    if digits_inside.lower() == 'y':
        chars += digits

    low_letters = input("Lowercase letters? (Yes - y, No - n): ")
    if low_letters.lower() == 'y':
        chars += lowercase_letters

    upp_letters = input("Uppercase letters? (Yes - y, No - n): ")
    if upp_letters.lower() == 'y':
        chars += uppercase_letters

    symbols = input("Include symbols? (Yes - y, No - n): ")
    if symbols.lower() == 'y':
        chars += punctuation

    if not chars:
        print("You need to select at least one character set!")
        return []

    all_passwords = []
    while how_much_passwords > 0:
        password = ''
        for _ in range(length):
            password += "".join(choice(chars))
        all_passwords.append(password)
        how_much_passwords -= 1

    print("\nPlease: ")
    return all_passwords


print(*generate_passwords(), sep='\n')
