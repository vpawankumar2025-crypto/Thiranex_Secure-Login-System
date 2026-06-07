# Secure Login System

A beginner-friendly Flask web application that demonstrates secure user registration and login using hashed passwords, input validation, session management, logout functionality, and optional demo 2FA. OWASP recommends strong password storage with modern hashing algorithms, parameterized database queries to prevent SQL injection, and careful session management to protect authenticated users.

## Features

- User registration and login
- Password hashing using Werkzeug's secure hash helpers
- Input validation for username, email, and password policy
- Protection from SQL injection through parameterized SQLite queries, which OWASP recommends as a primary defense.[web:71][web:76]
- Session-based authentication with logout support
- Optional demo 2FA code verification
- SQLite database for simple local storage

## Project structure

```text
secure-login-system/
├── app.py
├── requirements.txt
├── users.db
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── verify_2fa.html
│   └── dashboard.html
└── static/
    └── style.css
```

## Installation

```bash
git clone https://github.com/your-username/secure-login-system.git
cd secure-login-system
pip install -r requirements.txt
python app.py
```

## Usage

1. Open `http://127.0.0.1:5000/` in your browser.
2. Register a user account.
3. Log in using your credentials.
4. If 2FA is enabled during registration, enter the demo code shown after signup.
5. Access the dashboard and use logout to end the session.

## Security concepts used

- Password hashing protects stored passwords from plain-text exposure, and OWASP recommends modern password hashing approaches such as Argon2id, with scrypt or bcrypt as alternatives when Argon2id is not available.[web:10]
- Parameterized queries help separate code from user input and are OWASP's primary recommendation for preventing SQL injection.[web:71][web:76]
- Session handling is essential because weak session controls can expose authenticated accounts to hijacking and related attacks.[web:72]

## Notes

This project is an educational demo. For production use, add CSRF protection, secure cookie settings, rate limiting, email-based 2FA or authenticator-app TOTP, stronger password policy checks, account lockout, and environment-based secret management.[web:10][web:72]

## Author

**Pawan Kumar V**  
Cybersecurity Student | Python Security Projects | Ethical Hacking Enthusiast
