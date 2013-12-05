#!/usr/bin/python
"""
Assignment06 Dist Systems CS4520
Second part of entering a new club
enterNewClub -> [saveClub]
Author: Andrew Bocz
"""
import database
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
name = form.getlist("name")
desc = form.getlist("description")
grps = form.getlist("groups")
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
'''.format("Saving New Club")
if type(name[0]) != str or type(desc[0]) != str:
    print "<h1>Submit the Proper Data to Save</h1>"
    print "<p>Hit the back button to try again</p>"
    print "<p>{}</p>".format(type(name[0]))
elif len(name[0])<=0 or len(desc[0])<=0:
    print "<h1>Name and description must be filled out</h1>"
    print "<p>Hit the back button to try again</p>"
else:
    print "<h1>Saving New Club", name[0], "...</h1>"
    club = (name[0], desc[0])
    ident = database.saveNewClub(club)
    if grps:
        grps.insert(0, ident)
        database.updateGroups(grps)        
    print "<a href='enterNewClub.py'>Insert Another Club</a>"
print '''
</div>
</body>
</html>
'''
