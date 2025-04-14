def check_password_strength(password):
    criteria = 0

    # Length check
    if len(password) >= 8:
        criteria += 1

    # Uppercase check
    if any(char.isupper() for char in password):
        criteria += 1

    # Lowercase check
    if any(char.islower() for char in password):
        criteria += 1

    # Digit check
    if any(char.isdigit() for char in password):
        criteria += 1

    # Special character check
    if any(char in '!@#$' for char in password):
        criteria += 1

    # Final strength evaluation
    if criteria < 3:
        print('Weak')
    elif criteria <= 4:
        print('Moderate')
    else:
        print('Strong')
