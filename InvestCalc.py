import os
import datetime

typelist = ["SAVINGS","SHARE","BOND","OTHER"]

SAVINGS = 0
SHARE = 1
BOND = 2
OTHER = 3















class investment:
  InvestmentName = None
  InvestmentType = None
  ExpectedAER = None

  def __init__(self, InvName, InvType, ExpAER, InitVal, MonthIn):
  	self.InvestmentName = InvName
  	self.InvestmentType = InvType
  	self.ExpectedAER = float(ExpAER)
  	self.InitialValue = float(InitVal)
  	self.MonthlyDeposit = float(MonthIn)


  def printDeets(self):
  	print("--- "+ self.InvestmentName + " ---")
  	print(typelist[self.InvestmentType])
  	print("AER: " + self.ExpectedAER + "%")
  	print("Initial Value: " + self.InitialValue)
  	print("+" + self.MonthlyDeposit + " per Month")
  	print("")

  def calcToDate(self, months):
  	TempVal = self.InitialValue
  	for i in range(months):
  		TempVal = TempVal*(1 +(self.ExpectedAER/1200))
  		TempVal += self.MonthlyDeposit
  	print("in " + str(diffMonths) + " months time " + self.InvestmentName + " will be worth: £" + str(round(TempVal, 2)) + " (AER compounded monthly earning £" + str(round(TempVal - (self.InitialValue+(months*self.MonthlyDeposit)), 2)) + " interest)")
  	return TempVal

  def __str__(self):
  	return str(self.__class__) + ": " + str(self.__dict__)






# ~~~ MAIN ~~~ #

InvestmentList = []

os.system('color a')
print("/*****************************************************************/")
print("")
print("  InvestCalc v0.0000002                                       JRM")
print("")
print("  Commands:")
print("  add - create an investment")
print("  print - print all investments")
print("  forecast - calculate investment value in the future")
print("")
print("/*****************************************************************/")

while 1:
	print(">>>", end='')
	inputter = input()

	if inputter == "":
		pass

	elif inputter == "add":
		InvName = input('Name: ')
		print("Investment Type: SAVINGS")
		ExpAER = input('Expected AER: ')
		InitVal = input('Initial Value: ')
		MonthIn = input('Monthly Deposit: ')
		InvestmentList.append(investment(InvName, SAVINGS, ExpAER, InitVal, MonthIn))
		print("")
		
	elif inputter == "print":
		print("")
		for i in InvestmentList:
			i.printDeets()

	elif inputter == "forecast":
		endDateInput = input('Enter End Date(mm/yy): ')
		if len(endDateInput) == 5 and endDateInput[2] == "/":
			endDate = datetime.datetime(int(endDateInput[3:5]) + 2000, int(endDateInput[0:2]), 1)
			todayDate = datetime.datetime.today()
			diffMonths = endDate.month - todayDate.month + 12*(endDate.year - todayDate.year)
			totalVal = 0
			for i in InvestmentList:
				totalVal+= i.calcToDate(diffMonths)
			print("")
			print("Total: " + str(round(totalVal, 2)))

		else:
			print("Error")


	else:
		print("Error: Command not found")


