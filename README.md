* Workflow of the Project *

1. Password Input

* User enters a password through the application.
* The password is received for analysis.

2. Password Reuse Check

* The system checks whether the password has been used before.
* Previously used passwords are identified using their SHA-256 hash values stored in the database.
* A warning is displayed if the password has already been used.

3. Password Strength Analysis

The password is evaluated based on:

* Length of the password
* Presence of uppercase letters
* Presence of lowercase letters
* Presence of numbers
* Presence of special characters

4. Strength Classification

Based on the analysis score, the password is categorized as:

* Weak
* Medium
* Strong

5. Feedback Generation

* The system provides suggestions to improve password security.
* Missing security requirements are highlighted to the user.

6. Strong Password Suggestion

* If the password is weak or medium, the system generates a stronger password suggestion.
* The suggested password contains a mix of letters, numbers, and special characters.

7. Secure Password Storage

* Passwords are converted into SHA-256 hash values.
* Only hashed passwords are stored in the SQLite database.
* Plain-text passwords are never stored.

8. Result Display

* The final password strength is displayed.
* Security suggestions and warnings are shown.
* A strong password recommendation is provided when required.

* Technologies Used *

* Python
* SQLite
* Hashlib (SHA-256)
* Regular Expressions (re)
* Visual Studio Code

* Security Features *

* Password Strength Evaluation
* Password Reuse Prevention
* SHA-256 Password Hashing
* Secure Password Storage
* Strong Password Generation


CODE SCREENSHOT : 

<img width="1495" height="896" alt="Screenshot 2026-06-15 at 3 14 24 PM" src="https://github.com/user-attachments/assets/df138095-abe4-4837-87bd-9ba811efcae9" />

WEAK PASSWORD OUTPUT SCREENSHOT :

<img width="1494" height="896" alt="Screenshot 2026-06-15 at 3 15 20 PM" src="https://github.com/user-attachments/assets/bd0f829a-354b-46c2-92e7-583d2da35160" />

MEDIUM PASSWORD OUTPUT SCREENSHOT :

<img width="1496" height="893" alt="Screenshot 2026-06-15 at 3 16 18 PM" src="https://github.com/user-attachments/assets/a7680d94-43fb-4fd7-8e5c-7d7f88886f72" />

STRONG PASSWORD OUTPUT SCREENSHOT :

<img width="1492" height="902" alt="Screenshot 2026-06-15 at 3 18 52 PM" src="https://github.com/user-attachments/assets/5d731a52-397e-4a43-b4fe-41a6f1a54fed" />




