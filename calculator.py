while True:
    x = float(input("what is x? "))
    y = float(input("what is y? "))

    operator = input("What operation do you want to perform? (+, -, *, /): ")

    if operator == '+':
        result = x + y
        print(f"{x} + {y} = {result}")
    elif operator == '-':
        result = x - y
        print(f"{x} - {y} = {result}")
    elif operator == '*':
        result = x * y
        print(f"{x} * {y} = {result}")
    elif operator == '/':
        if y == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = x / y
            print(f"{x} / {y} = {result}")
    else:
        print("invalid operator.")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != 'yes':
        break