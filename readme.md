# User Management CLI Tool

A simple terminal-based User Management System built with Python. It supports creating, viewing, and removing users using keyboard input. Admin access is required to view the user list.

---

## Project Structure
```bash
user_management_project/
├── main.py
├── user_manager.py
└── README.md
```

## How to Run

1. **Install dependencies:**  
   This project uses the `keyboard` module. You can install it with:

```bash
   pip install keyboard
   python main.py
```

## Controls

| **Key** | **Action**                    |
|--------:|-------------------------------|
| `S`     | Show all users (admin only)   |
| `C`     | Create a new user             |
| `R`     | Remove an existing user       |
| `Q`     | Quit the application          |

## Admin Password

To view the user list, enter the admin password: 1234

## Features

- **Add new users** with unique usernames
- **Secure removal** of users with password confirmation
- **Admin-only access** to view all users
- **Keyboard-based input handling** for simple interaction

---

## Notes

- All passwords are stored as **integers** for simplicity
- This version **does not persist** user data after the program exits


