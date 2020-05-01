#######################################################################################
# Main Program Module: CaculateTaxes.py
# Written by: Selene F Tolbert
# Version: 1, 4/12/2020
#######################################################################################

#system imports
import csv

#custom imports
import functionsmodule
import classesmodule

# gather input from user
print("WELCOME, Lets Calculate how much you will pay in taxes!\n")

# user name
userName = input("Please enter your Name and Lastname: ")

# user status (single or married) to identify the tax brackets to use
status = input("Are you Filling as Single or Married: ")
userStatus = status.strip()
userStatus = status.lower()
if (userStatus != "single" and userStatus != "married"):
	print("-- You entered and incorrect Filling Status, ", userStatus, ". Exiting program.")
	exit()

# taxable income (yearly salary)
tmpVal = input("What is your Yearly Salary: ")
if tmpVal.isnumeric():
	amtIncome = int(tmpVal)
else:
	print("-- You entered and invalid Salary. Exiting program")
	exit()

# instantiate the person class as a user object
user = classesmodule.Person(userName, userStatus, amtIncome)

# print class members attributes
user.printinput()

salary_left = float(user.amtIncome)
tot_taxes = 0

# determine tax bracket to load (single or married)
if user.userStatus == "single":
	input_file = csv.DictReader(open("SingleTaxBrakets.csv"))

else:
	input_file = csv.DictReader(open("MarriedTaxBrakets.csv"))

# traverse read input file to pull each rows tax details
for row in input_file:
	tx_rate    = float(row["Tax Rate"])
	tx_bracket = str(row["Tax Bracket"])
	st_range   = int(row["Start Range"])
	end_range  = int(row["End Range"])

	# invoke function to calculate tax brackets based on taxable income
	ret_val    = functionsmodule.get_taxbrackets(salary_left, tx_rate, tx_bracket, st_range, end_range)

	# use taxes return value to get total sum of all taxes per tax brackets
	tot_taxes  += ret_val

	salary_left -= (end_range - st_range)
	if salary_left <= 0:
		# break out of for look
		break
	
print ("\tTotal Amount of Taxes to pay this year: ${:,.2f}".format(tot_taxes))

#delete instantiated object
del user

