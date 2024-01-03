


def login():
    user_register = {
        "admin" : "123",
        "sa" : "root",
        "paco" : "222"
    }

    #request user and password
    user = input("Enter user: ")
    password = input("Enter password: ")

    #Valid user and pass
    if user in user_register and password == user_register[user]:
        print("login successful", " !Welcome¡", user)
    else:
        print("Incorret")
        