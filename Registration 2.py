def register_user(username, password):
    users = {}
    
    if username in users:
        return False, "Username already exists!"
    else:
        users[username] = password
        return True, "Registration successful!"

def main():
    print("Welcome to the Bank App Registration")
    
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    
    success, message = register_user(username, password)
    print(message)
