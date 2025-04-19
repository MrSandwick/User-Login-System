import keyboard

userList = {}
print("\nPlease press a corresponding key:\n" \
"S to Show list\n" \
"C to Create new user\n" \
"R to Remove a user\n" \
"Q to Quit")

while True:

    key = keyboard.read_key().lower()

    if key == "s":
        try:
            rootPassword = int(input("Admin password:\n"))
        except ValueError:
            print("Invalid password! Must be a number.\n")
            continue
        if rootPassword == 1234:
            print(f"User List:\n{userList}")
        else:
            print("Incorrect admin password.\n")

    elif key == "c":
        login = input("Login:\n").strip()
        if login in userList:
            print("This user already exists.\n")
            continue
        try:
            password = int(input("Password:\n"))
        except ValueError:
            print("Invalid input! Password must be a number.\n")
            continue
        userList[login] = password
        print(f"New user '{login}' was added.\n")

    elif key == "r":
        login = input("Enter your login:\n").strip()
        if login in userList:
            try:
                password = int(input("Password:\n"))
            except ValueError:
                print("Invalid input! Password must be a number.\n")
                continue
            if userList.get(login) == password:
                userAgree = input("Are you sure you want to delete your account?\nYes/No? ").lower().strip()
                if userAgree == "yes":
                    del userList[login]
                    print(f"User '{login}' was removed.\n")
                else:
                    print("Account was not deleted.\n")
            else:
                print("Oops, wrong password.\n")
        else:
            print("Sorry, that user does not exist.\n")

    elif key == "q":
        print("Exiting... Goodbye!\n")
        break

    else:
        print("Invalid key! Please use S, C, R, or Q.\n")