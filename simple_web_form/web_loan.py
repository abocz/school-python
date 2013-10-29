#!/usr/bin/python
import cgitb
cgitb.enable()
import cgi
import math

class FormInException(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)
class Loan(object):
	# computes the remaining balance
	def remainingBalance(self, month):
		if month < 1:
			raise FormInException(1)
			print '''HTTP/1.1 501 Not Implemented 
Content-type: text/html

'''
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
# get the input values
form = cgi.FieldStorage()
balance = float(form.getfirst("balance",0))
term = int(form.getfirst("term", 10))
rate = float(form.getfirst("rate", 11))
# setup the loan object
loan_object = Loan(balance, term, rate)
loan_object.computeMonthlyPayment()
print "Content-Type: text/html; charset=UTF-8"
print ""
print '''
<!DOCTYPE html>
<html>
    <head>
        <title>Loan Table</title>
        <link rel="Stylesheet" type="text/css" href="/style1-assignment05.css"/>
    </head>
    <body>
        <h1>Loan Table</h1>
'''
print "<h3>Input Values:</h3><p>Balance: ",loan_object.balance,"</p><p>Term Length(in months): ",loan_object.term,"</p><p>Rate(as a percent):",loan_object.rate
# table html
print "<table class='grid'>"
print "<tr>"

# print column headers
print "<th>Month</th><th>Balance In</th><th>Interest</th><th>Payment</th><th>Balance Out</th>"

print "</tr>"
month=1
for x in range (1, loan_object.term+1):
	print "<tr><td>{0:>5}</td><td>{1:>15.2f}</td><td>{2:>15.2f}</td><td>{3:>15.2f}</td><td>{4:>15.2f}</td></tr>".format(month, loan_object.remainingBalance(month), loan_object.interestAccrued(month),loan_object.payment, loan_object.remainingBalance(month+1) )
	month=month+1
# end table html
print "</table>"

print '''      
    </body>
</html>
'''

