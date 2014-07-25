class Loan(object):
	# computes the remaining balance
	def remainingBalance(self, month):
		if month < 1:
			raise ValueError("month must be positive")
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
		if (balance <= 0) or (term <= 0) or (rate <= 0):
			raise ValueError("can't be zero")
		self.balance = balance
		self.term = term
		self.rate = rate
		# convert annual rate to monthly rate, also casting it
		self.monthly_rate = rate / (100.0 * 12)
