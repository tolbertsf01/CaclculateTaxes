#######################################################################################
# Module: classesmodule.py
# Written by: Selene F Tolbert
# Version: 1, 4/12/2020
#######################################################################################

class Person: 
  def __init__(self, userName, userStatus, amtIncome):
    self.userName = userName
    self.userStatus = userStatus
    self.amtIncome = amtIncome
    

  def printinput(self):
    print("\n\tYour Fullname: " + self.userName + "\n",
  	"\tYour Filling Status: " + self.userStatus + "\n",
	  "\tYour Taxable Income (Yearly Salary): ${:,.2f}".format(self.amtIncome))
    