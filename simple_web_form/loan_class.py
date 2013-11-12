# Assignment 2 CS 4520 Andrew Bocz
# Loan object class
import math

class Loan(object):
	# computes the remaining balance
	def remainingBalance(self, month):
		if month < 1:
			return 0
		elif month == 1:
			return self.balance
		else:
			temp_bal = self.balance
			return self.remainingBalance(month-1) + self.interestAccrued(month-1) - self.payment
	# computes the interest accrued
	def interestAccrued(self, month):
		if month == 1:
			return self.balance * self.monthly_rate
		else:
			return self.remainingBalance(month) * self.monthly_rate
	# computes the monthly payment by dividing the annual rate by the term length
	def computeMonthlyPayment(self):
		self.payment = self.balance * ( self.monthly_rate / (1 - (1 + self.monthly_rate) ** (-self.term)))
		return round(self.payment, 2)
	# init function	
	def __init__(self, balance, term, rate):
		self.balance = balance
		self.term = term
		self.rate = rate
		# convert annual rate to monthly rate, also casting it
		self.monthly_rate = rate / (100.0 * 12)
	# format the print string function
	def __str__(self):
		fmt = '''
	Initial Balance:		{0:10.2f}
	Term Length:			{1:10d}
	Annual Rate:			{2:10.5f} 
		'''
		return fmt.format(self.balance, self.term, self.rate)
