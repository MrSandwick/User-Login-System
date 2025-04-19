import keyboard

userList = {}

while True:
    # login = input("Login\n")
    # password = int(input("Password\n"))
    # userList[login] = password
    # print(f"{login} added.\n")
    print("Please press corresponding key\n" \
    "S to Show list\n" \
    "C to Create new user\n" \
    "R to Remove a user\n" \
    "Q to quit")
    buttonPressed = keyboard.read_event()
    if buttonPressed.event_type == keyboard.KEY_DOWN:
        key = buttonPressed.name.lower()
        if key == "s":
            try:
                rootPassword = int(input("Admin password:\n"))
            except ValueError:
                print("Invalid password! Must be a number.\n")
                continue
            if rootPassword == 1234:
                print(f"List:\n {userList}")
        elif key == "c":
            login = input("Login:\n")
            try:
                password = int(input("Password:\n"))
            except ValueError:
                print("Invalid input! Password must be a number.\n")
                continue
            userList[login] = password
            print(f"New user - {login} was added")
        elif key == "r":
            login = input("Enter your login:\n")
            if login in userList:
                try:
                    password = int(input("Password:\n"))
                except ValueError:
                    print("Invalid input! Password must be a number.\n")
                    continue
                if userList.get(login) == password:
                    userAgree = input("Are you sure you want to delete your account?\nYes/No? ")
                    userAgree = userAgree.lower()
                    if userAgree == "yes":
                        del userList[login]
                        print(f"{login} removed.\n")
                    else:
                        print("Account was not deleted.\n")
                else:
                    print("Oops, wrong password")
            else:
                print("Sorry, that user does not exist")
        elif key == "q":
            break
        else:
            print("Dude, look what you typing")
