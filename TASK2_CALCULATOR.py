num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Choose an operation: +  -  *  /")
operation = input("Enter your choice: ")
if operation == "+":
    result = num1 + num2
    print("The result is:", result)
elif operation == "-":
    result = num1 - num2
    print("The result is:", result)
elif operation == "*":
    result = num1 * num2
    print("The result is:", result)
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("The result is:", result)
    else:
        print("Oops! Division by zero is not allowed.")
else:
    print("That operation is not recognized.")
