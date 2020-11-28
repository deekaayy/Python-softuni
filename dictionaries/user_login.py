unsuccessful_logins=0
users = {}

while True:
    user_info = input()
    if user_info=="login":
        break

    user_split=user_info.split(" -> ")
    user = user_split[0]
    user_password = user_split[1]

    if user not in users:
        users[user]=user_password

while True:
    user_login = input()
    if user_login == "end":
        break

    user_login_split = user_login.split(" -> ")
    username = user_login_split[0]
    username_pass = user_login_split[1]

    if username in users:
        if (users[username]==username_pass):
            print(f"{username}: logged in successfully")
        else:
            unsuccessful_logins=unsuccessful_logins+1
            print(f"{username}: login failed")
    else:
        unsuccessful_logins = unsuccessful_logins + 1
        print(f"{username}: login failed")

print(f"unsuccessful login attempts: {unsuccessful_logins}")