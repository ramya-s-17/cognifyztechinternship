import re

def check_password_strength(password):
    strength_criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }
    
    strength_score = sum(strength_criteria.values())
    
    if strength_score == 5:
        return "Strong password"
    elif strength_score >= 3:
        return "Moderate password"
    else:
        return "Weak password"

# Continuous input loop
while True:
    password = input("Enter a password to check its strength (or type 'exit' to quit): ")
    if password.lower() == 'exit':
        break
    print(check_password_strength(password))
