class Account:

    def __init__(self):
        self.username = input("Username: ")
        self.password = input("Password: ")
        self.password_confirmation = input("Confirm Password: ")
        self.email = input("Email: ")

    def check_password(self):
        if self.password == self.password_confirmation:
            print("Your account has been saved.")
            return True
        else:
            print("Error: Your passwords do not match.")
            return False

    def save_account(self):
        f = open("data.txt", "a")
        f.write(self.username)
        f.write(",")
        f.write(self.password)
        f.write(",")
        f.write(self.email)
        f.write("\n")
        f.close()


has_account = input("Do you have an account? (y/n): ")

if has_account == "y":
    username = input("Username: ")
    password = input("Password: ")
elif has_account == "n":
    print("Okay, you will now create a new account.")
    new_account = Account()

    if new_account.check_password():
        new_account.save_account()
    exit()
else:
    print("Error: Enter 'y' or 'n' only")
    exit()

data = open("data.txt", "r")

with open("data.txt") as f:
    for line in f:
        information = line.split(",")

        if username == information[0] and password == information[1]:
            login_status = True
        else:
            login_status = False
data.close()

if login_status == True:
    print("Login Status: Success")
else:
    print("Login Status: Failure")