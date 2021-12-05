def accept_login(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and password in users.get(username):
        return True
    else:
        return False

users = {
    "user1" : "password1",
    "user2" : "password2",
    "user3" : "password3"}
if accept_login(users) :
    print("login successful!")
else:
    print("login failed...")