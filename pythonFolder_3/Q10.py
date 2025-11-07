# Q10. Handle multiple exceptions in a single try block.

try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))   
    result = num1 / num2
    print("Result: ", result) 

except ValueError:
    print("Invalid input. Please enter valid numbers.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")       

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Program execution completed.")