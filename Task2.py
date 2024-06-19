
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter choice (Add/Sub/Mul/Div): ")

    if choice in ('Add', 'Sub', 'Mul', 'Div'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 'Add':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 'Sub':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 'Mul':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == 'Div':
            print(num1, "/", num2, "=", divide(num1, num2))

        next_calculation = input("Let's do next calculation? \n Yes \n No ")
        if next_calculation == "No":
          break
    else:
        print("Invalid Input")   

