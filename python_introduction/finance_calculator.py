
# Prompt user for monthly income
income = float(input("Enter your monthly income: "))

# Prompt user for monthly expenses
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
Monthly_Savings = income - expenses

# Project annual savings with 5% interest
Annual_Savings = Monthly_Savings * 12
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)

# Display results
print("Your monthly savings are $", Monthly_Savings, ".", sep="")
print("Projected savings after one year, with interest, is: $", Projected_Savings, ".", sep="")
