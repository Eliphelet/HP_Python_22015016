import re

def signup():
    while True:
        username = input("Enter a username: ")
        with open('filesignup.txt', 'r') as f:
            for line in f:
                if username in line:
                    print("This username already exists. Please choose another one.")
                    break
            else:
                break
    
    while True:
        password = input("Enter a password (must contain at least one digit and one letter and have a length of 6-12 characters): ")
        if re.match(r'^(?=.*[0-9])(?=.*[a-zA-Z])[a-zA-Z0-9]{6,12}$', password):
            break
        else:
            print("Invalid password. Please enter a password that contains at least one digit and one letter and has a length of 6-12 characters.")
    
    with open('filesignup.txt', 'a') as f:
        f.write(f"{username}:{password}\n")
    print("You have successfully signed up.")

def signin():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        with open('filesignup.txt', 'r') as f:
            for line in f:
                if line.startswith(username + ":"):
                    saved_password = line.split(":")[1].rstrip()
                    if saved_password == password:
                        print("You have successfully signed in.")
                        with open('filesignin.txt', 'a') as f2:
                            f2.write(f"{username}\n")
                        return
                    else:
                        print("Incorrect password.")
                    break
            else:
                print("There is no account with that username.")
        answer = input("Do you want to try again? (y/n) ")
        if answer.lower() != "y":
            break

while True:
    print("1. Sign up")
    print("2. Sign in")
    print("3. Quit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        signup()
    elif choice == "2":
        signin()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3."
