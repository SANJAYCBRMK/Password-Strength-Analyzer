from password_checker import analyze_password
from password_generator import generate_password
from password_history import password_used, save_password

password = input("Enter password: ")

if password_used(password):
    print("Warning: Password has been used before!")
else:
    save_password(password)

strength, feedback = analyze_password(password)

print("\nPassword Strength:", strength)

if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print("-", item)

if strength != "Strong":
    print("\nSuggested Strong Password:")
    print(generate_password())