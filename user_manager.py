user_list = {}

def show_users():
    try:
        root_password = int(input("Admin password:\n"))
    except ValueError:
        print("Invalid password! Must be a number.\n")
        return
    if root_password == 1234:
        print(f"User List:\n{user_list}\n")
    else:
        print("Incorrect admin password.\n")

def create_user():
    login = input("Login:\n").strip()
    if login in user_list:
        print("This user already exists.\n")
        return
    try:
        password = int(input("Password:\n"))
    except ValueError:
        print("Invalid input! Password must be a number.\n")
        return
    user_list[login] = password
    print(f"New user '{login}' was added.\n")

def remove_user():
    login = input("Enter your login:\n").strip()
    if login not in user_list:
        print("Sorry, that user does not exist.\n")
        return
    try:
        password = int(input("Password:\n"))
    except ValueError:
        print("Invalid input! Password must be a number.\n")
        return
    if user_list.get(login) == password:
        user_agree = input("Are you sure you want to delete your account?\nYes/No? ").lower().strip()
        if user_agree == "yes":
            del user_list[login]
            print(f"User '{login}' was removed.\n")
        else:
            print("Account was not deleted.\n")
    else:
        print("Oops, wrong password.\n")