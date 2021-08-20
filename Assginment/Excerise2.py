#Exercise 2
#Write a function calculation() such that it can accept two variables and 
#calculate the addition and subtraction of them.
#And also,it must return both addition and subtraction 
#in a single return call.

def login():
    username = input("Username :")
    password = input("Password :")
    while (username != "admin" and password != "file"):
        username = input("Username :").capitalize
        password = input("Password :")
    print("Login success")
    return True

def showMenu():
    print("Calculator".center(20,"-"))
    print("1.Calculate")
    print("2.Exit")

def menuSelect():
    userSelected = int(input(":"))
    return userSelected

def cal(a, b):
    return a+b, a-b

def show(x,y):
    add, sub = cal(x, y)
    print("Addition:",add)
    print("Subtraction:",sub)

if login()==True:
    showMenu()
    menu = menuSelect()
    if menu == 1:
        a = int(input("NUMBER1:"))
        b = int(input("NUMBER2:"))
        show(a,b)
    elif menu == 2:
        print("GOODBYE".center(20,"-"))
        print("(^_^)".center(20))
    else:
        print("Error")