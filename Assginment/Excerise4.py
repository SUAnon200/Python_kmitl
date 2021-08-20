def login():
    username = input("Username :")
    password = input("Password :")
    while (username != "admin" and password != "file"):
        username = input("Username :").capitalize
        password = input("Password :")
    print("Login success")
    return True
if login()==True:
    print("Welcome".center(30,"-"))
    a = float(input("Input first number: "))
    b = float(input("Input second number: "))
    c = float(input("Input third number: "))
    if a > b:
        if a < c:
            median = a
        elif b > c:
            median = b
        else:
            median = c
    else:
        if a > c:
            median = a
        elif b < c:
            median = b
        else:
            median = c

    print("List of data".center(20,"-"))
    print("[",a,b,c,"]")
    print("The median is", median)