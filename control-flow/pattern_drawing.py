# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Validate positive integer
if size <= 0:
    print("Please enter a positive integer.")
else:
    row = 0
    # Outer loop (while) for rows
    while row < size:
        # Inner loop (for) for columns
        for col in range(size):
            print("*", end="")  # Print asterisks side by side
        print()  # Move to the next line after each row
        row += 1
