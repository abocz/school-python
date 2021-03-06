# Assignment 2 CS 4520 - Script
# Andrew Bocz

from sys import argv
from loan_class import Loan


if len(argv) != 4:
	raise ValueError("wrong number of arguements")

balance = float(argv[1])
term = int(argv[2])
rate = float(argv[3])

print
print "Loan Caclulator Script"

loan_object = Loan(balance, term, rate)
print loan_object
loan_object.computeMonthlyPayment()

print "{0:>5}{1:>15}{2:>15}{3:>15}{4:>15}".format("Month", "Balance In", "Interest", "Payment", "Balance Out")
month=1
for x in range (1, loan_object.term+1):
	print "{0:>5}{1:>15.2f}{2:>15.2f}{3:>15.2f}{4:>15.2f}".format(month, loan_object.remainingBalance(month), loan_object.interestAccrued(month),loan_object.payment, loan_object.remainingBalance(month+1) )
	month=month+1
