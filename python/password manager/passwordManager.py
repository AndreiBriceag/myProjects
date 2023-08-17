from cryptography.fernet import Fernet

masterPassword = input("Insert the master password: ")
key_file_path = "pwManager/key.key"

def writeKey():
    key = Fernet.generate_key()
    with open(key_file_path, "wb") as keyFile:
        keyFile.write(key)

writeKey()

def view():
    with open("pwManager/passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("User:", user, "| Password:", password)

def add():
    name = input("Account Name: ")
    password = input("Password: ")
    
    with open("pwManager/passwords.txt", "a") as f:
        f.write(name + "|" + password + "\n")

while True:
    mode = input("Do you want to add a new password or view existing passords? Type add/view or q to quit. ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue