import keyboard
import user_manager

def main():
    print("\nPlease press a corresponding key:\n" \
            "S to Show list\n" \
            "C to Create new user\n" \
            "R to Remove a user\n" \
            "Q to Quit\n")

    while True:
        key = keyboard.read_key().lower()

        if key == "s":
            user_manager.show_users()
        elif key == "c":
            user_manager.create_user()
        elif key == "r":
            user_manager.remove_user()
        elif key == "q":
            print("Exiting... Goodbye!\n")
            break
        else:
            print("Invalid key! Please use S, C, R, or Q.\n")

if __name__ == "__main__":
    main()
