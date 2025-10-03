# Q3. Handle a ZeroDivisionError using try-except.

try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
    print("Result: ", result)

except ZeroDivisionError:
    print ( f" Division by zero is not allowed.")
except ValueError:
    print("Invalid input. Please enter valid numbers.")

    