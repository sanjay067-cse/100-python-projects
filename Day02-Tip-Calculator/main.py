# Welcome message to the user
print("***** Welcome to the Tip Calculator! *****")

# Taking input from the user
bill = float(input("What was the total bill? $"))
tip = float(input("How much percentage of tip would you like to give? 10, 12, or 15? "))
people =int(input("How many people to split the bill? "))

# Calculating tip in amount
tip = float(bill * (tip / 100))

# Adding tip to the old bill to get the new bill
new_bill = bill + tip

# Splitting the new bill among specified no. of peoples given by the user and
each = new_bill / people

# Calculating and printing the final bill after rounding the split bill to two decimal places
final = round(each, 2)
print(f"Each person should pay: ${final} ")
