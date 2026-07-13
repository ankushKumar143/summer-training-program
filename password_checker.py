import re
def check_password_strength(password):
    score = 0
    suggestions = []

    #length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Password should be at least 8 characters long.")

    #digits
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Password should contain at least one digit.")

    #uppercase
    if re.search(r"[A-Z]",password):
        score += 1
    else:
        suggestions.append("Password should contain at least one uppercase letter.")

    #lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Password should contain at least one lowercase letter.")

    #special characters
    if re.search(r"[!@#$%^&*()_+=}|;:,.<>/?-]", password):
        score += 1
    else:
        suggestions.append("Password should contain at least one special character.")

    return score, suggestions

password = input("Enter a password: ")
score, suggestions = check_password_strength(password)

if score <= 2:
    print("Weak")
elif score == 3 or score == 4:
    print("Medium")
else:
    print("Strong")

for s in suggestions:
    print(s)