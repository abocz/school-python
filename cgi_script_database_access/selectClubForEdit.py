#!/usr/bin/python

"""

Assignment06 Dist Systems CS4520

First part of editing a new club

[selectClubForEdit] -> editSelectClub -> editClub

Author: Andrew Bocz

"""

import database

import cgitb

cgitb.enable()

print "Content-Type: text/html; charset=UTF-8"

print ""

print '''

<!DOCTYPE html>

<html>

    <head>

        <title>{}</title>

        <link rel="stylesheet" type="text/css" href="/python-html/clubStyle.css"/>

    </head>

    <body>

    <div id='content'>

'''.format("Select Club")



print "<h1>Select a Club to Display</h1>"



print "<form method='get' action='editSelectedClub.py'>"

print "<select name='chosen'>"

clubs = database.getListOfClubs()

for club in clubs:

    print "<option value='{}'>{}</option>".format(club[0], club[1])

print "</select>"

print "<p><input type='submit' value='Display' /></p>"

print "</form>"

print '''

</div>

</body>

</html>

'''
