import getpass

def check_default_credentials(username, password):
    return username == 'admin' and password == 'admin'

def force_password_change():
    print("You must change the default password.")
    new_password = getpass.getpass("Enter new password: ")
    confirm_password = getpass.getpass("Confirm new password: ")
    if new_password == confirm_password:
        print("Password changed successfully.")
    else:
        print("Passwords do not match. Try again.")
        force_password_change()

def main():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    if check_default_credentials(username, password):
        force_password_change()
    else:
        print("Login successful.")

if __name__ == '__main__':
    main()
