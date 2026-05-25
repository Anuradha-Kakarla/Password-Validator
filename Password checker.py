password = input("Enter password: ")

if (len(password) >= 8 and
    any(char.isupper() for char in password) and
    any(char.islower() for char in password) and
    any(char.isdigit() for char in password) and
    any(char in "!@#$%^&*" for char in password)):

    print("Strong Password")

else:
    print("Password must contain:")
    print("at least 8 characters: include uppercase , lowercase , number , special character")