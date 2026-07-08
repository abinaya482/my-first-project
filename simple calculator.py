print("Simple Calculator")
num1 = float(input("Enter first number: "))
operators = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))
if operators == '+':
    print("Result: ", num1 + num2)
elif operators == '-':
    print("Result: ", num1 - num2)
elif operators == '*':
    print("Result: ", num1 * num2)
elif operators == '/':
    if num2 != 0:
        print("Result: ", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator")