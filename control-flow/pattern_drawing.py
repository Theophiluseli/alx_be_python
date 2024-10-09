# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize a variable for the row count
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks in the current row
    for col in range(size):
        print("*", end=" ")  # Print asterisks side by side
    
    print()  # Print a newline character to move to the next row
    row += 1  # Increment the row count
