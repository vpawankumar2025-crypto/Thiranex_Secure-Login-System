"""
Task-04: Secure Login System
A simple console-based login system with username/password validation,
limited login attempts, account lockout, and secure feedback.
"""

import hashlib
import getpass
import time


# Demo user database
# In real applications, never store plain-text passwords.
users = {
    "pawan": hashlib.sha256("Pawan@123".encode()).hexdigest(),
    "admin": hashlib.sha256("Admin@2026".encode()).hexdigest()
}

MAX_ATTEMPTS = 3
LOCK_TIME = 10  # seconds


def hash_password(password):
    """Return SHA-256 hash of the password."""
    return hashlib.sha256(password.encode()).hexdigest()


def check_password_strength(password):
    """Basic password strength check for login registration or password change."""
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add at least one digit.")

    if any(not c.isalnum() for c in password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }


def register_user():
    """Register a new user with password validation."""
    print("\n=== User Registration ===")
    username = input("Enter a new username: ").strip()

    if not username:
        print("Username cannot be empty.")
        return

    if username in users:
        print("Username already exists.")
        return

    password = getpass.getpass("Enter a new password: ")
    result = check_password_strength(password)

    print(f"\nPassword Strength: {result['strength']} ({result['score']}/5)")
    for msg in result["feedback"]:
        print(f"- {msg}")

    if result["strength"] == "Weak":
        print("Please choose a stronger password.")
        return

    confirm_password = getpass.getpass("Confirm password: ")
    if password != confirm_password:
        print("Passwords do not match.")
        return

    users[username] = hash_password(password)
    print("Registration successful!")


def login_user():
    """Login a user with limited attempts and lockout."""
    print("\n=== Secure Login ===")
    username = input("Username: ").strip()

    if username not in users:
        print("Invalid username or password.")
        return

    attempts = 0

    while attempts < MAX_ATTEMPTS:
        password = getpass.getpass("Password: ")
        entered_hash = hash_password(password)

        if entered_hash == users[username]:
            print(f"\nWelcome, {username}! Login successful.")
            return
        else:
            attempts += 1
            remaining = MAX_ATTEMPTS - attempts
            print(f"Invalid username or password. Attempts left: {remaining}")

    print(f"\nToo many failed attempts. Account temporarily locked for {LOCK_TIME} seconds.")
    time.sleep(LOCK_TIME)
    print("You may try again now.")


def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("       Secure Login System")
    print("=" * 40)
    print("1. Register")
    print("2. Login")
    print("3. Exit")


def main():
    """Main program loop."""
    while True:
        show_menu()
        choice = input("\nEnter your choice (1/2/3): ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
