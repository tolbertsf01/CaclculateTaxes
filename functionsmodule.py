#######################################################################################
# Module: functionsmodule.py
# Written by: Selene F Tolbert
# Version: 1, 4/12/2020
#######################################################################################

# Function:	get_taxbrackets
# Purpose:	using the taxable income (yearly salary), alloocates it to the respective tax bracket
# 			and calculates the tax to be paid for such allocated tax bracket
# Return: 	total amount of taxes per tax bracket
def get_taxbrackets(salary_left, tax_rate, tax_bracket, start_income_range, end_income_range):

	# calculate the total amount of each tax bracket
	bracket_amt = float(end_income_range - start_income_range)

	if salary_left > 0:
		if salary_left > bracket_amt:
			currency_amt = bracket_amt
			tot_taxes = (bracket_amt * tax_rate)
		else:
			currency_amt = salary_left
			tot_taxes = (salary_left * tax_rate)

		print("\t${:,.2f}".format(currency_amt), "of your Taxable Income is taxed at", tax_bracket, ". For tax dollars amount of ${:,.2f}".format(tot_taxes))

		# return the total amout of taxes per tax bracket
		return tot_taxes
