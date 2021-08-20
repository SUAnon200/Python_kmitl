#Exercise 3: Write a function that takes the lengths of the two shorter 
#sides of a  righttriangle  as  its  parameters.  
#Return  the hypotenuseof  the  triangle, computed using Pythagorean 
#theorem, as the function’s result. Note that the lengths of the shorter 
#sides of a right triangle are read  as the user inputs, uses 
#your function to compute the length of the hypotenuse, and displays the result.

import math
def login():
    username = input("Username :")
    password = input("Password :")
    while (username != "admin" and password != "file"):
        username = input("Username :").capitalize
        password = input("Password :")
    print("Login success")
    return True

def cal():
    print("Welcome to Programs\nInput lengths of shorter triangle sides:")
    a = float(input("a: "))
    b = float(input("b: "))
    c = math.sqrt(a**2 + b**2)
    print("The length of the hypotenuse is:", c )

if login()==True:
    cal()