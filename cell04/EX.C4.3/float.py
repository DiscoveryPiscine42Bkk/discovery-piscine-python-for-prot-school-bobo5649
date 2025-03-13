try:
    number = float(input("Give me a number: "))
    if number == int(number):
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("Invalid input. Please enter a number.")