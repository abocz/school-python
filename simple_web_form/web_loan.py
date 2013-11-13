#!/usr/bin/python
import cgitb
cgitb.enable()
import cgi
import math
from loan_class import Loan
from error_page import errorPage


# get the input values from the form
form = cgi.FieldStorage()
balance = float(form.getfirst("balance",0))
term = int(form.getfirst("term", 0))
rate = float(form.getfirst("rate", 0))

# start html
print "Content-Type: text/html; charset=UTF-8"
print ""

# check for error
if (balance <= 0) or (term <= 0) or (rate <= 0):
	errorPage("No blank fields allowed. Retry form.")	
	quit()

# setup the loan object
loan_object = Loan(balance, term, rate)
loan_object.computeMonthlyPayment()

# display all html
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

