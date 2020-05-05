with open('auth.txt', 'r') as users:
    for line in users:
        username, password = line.split(',')
        print("Welcome, before you get started please enter your username")
        supplied_username = input()
        if username == supplied_username:
            print("Please enter you password")
            supplied_password = input()
            if password == supplied_password:
                print("Login Successful, the game will start now ")
                exec(open("game.py").read())
            else:
                print("Incorrect Password")
        else:
            print("Incorrect Username")