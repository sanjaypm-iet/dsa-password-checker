def min_changes(password):
    changes = 0

    # Check length
    if len(password) < 8:
        changes += (8 - len(password))

    # Flags
    has_upper = False
    has_lower = False
    has_digit = False

    # Traverse string
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True

    # Count missing types
    if not has_upper:
        changes += 1
    if not has_lower:
        changes += 1
    if not has_digit:
        changes += 1

    return changes


pwd = input("Enter password: ")
print("Minimum changes required:", min_changes(pwd))