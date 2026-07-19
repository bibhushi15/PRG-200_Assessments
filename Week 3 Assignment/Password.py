passwords = ["hello", "Hello123", "H3ll0@World", "12345678", "MyP@ss!"]
special_characters = "!@#$%^&*"
for password in passwords:
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False
    for character in password:
        if character.isupper():
            has_uppercase = True
        if character.islower():
            has_lowercase = True
        if character.isdigit():
            has_digit = True
        if character in special_characters:
            has_special = True
    print(f"\nPassword: {password}")
    if len(password) >= 8 and has_uppercase and has_lowercase and has_digit and has_special:
        print("Strong password")
    else:
        print("Weak password")
        print("Missing criteria:")
        if len(password) < 8:
            print("- At least 8 characters")
        if not has_uppercase:
            print("- At least one uppercase letter")
        if not has_lowercase:
            print("- At least one lowercase letter")
        if not has_digit:
            print("- At least one digit")
        if not has_special:
            print("- At least one special character")