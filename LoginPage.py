def validate_login(username, password):

    valid_username = "user"
    valid_password = "pass"
    
    if username == valid_username and password == valid_password:
        return True
    else:
        return False

def main():
    print("Welcome to the Bank App Login")
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if validate_login(username, password):
        print("Login Successful! Welcome to the Bank App!")
    else:
        print("Login Failed! Invalid username or password.")
