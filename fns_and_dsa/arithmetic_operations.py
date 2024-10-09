# Define the perform_operation function
def perform_operation(num1, num2, operation):
    # Check which operation is requested and perform the corresponding arithmetic operation
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        # Handle division by zero
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation."
