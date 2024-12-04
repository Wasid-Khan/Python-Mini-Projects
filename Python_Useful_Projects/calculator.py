import os

from django.db.models.fields import return_None

choice = True
while choice:
    operator = input("Enter your operator: (+ - * /): ")

    num_1 = float(input("Enter first number: "))
    num_2 = float(input("Enter second number: "))

    if operator == "+":
        result = num_1 + num_2
    elif operator == "-":
        result = num_1 - num_2
    elif operator == "*":
        result = num_1 * num_2
    elif operator == "/":
        if num_1 != 0:
            result = num_1 / num_2
        else:
            print("You cannot divide by zero")
    else:
        print("Invalid operator")

    print("Result for ", num_1, "+", num_2, "=", result)

    print("Do you want to continue? (y/n): ")
    choice = input().lower()
    if choice == "y":
        choice = True
    else:
        choice = False