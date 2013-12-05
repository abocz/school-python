#!/usr/bin/python
"""
Assignment06 Dist Systems CS4520
Third part of editing a new club
selectClubForEdit -> editSelectClub -> [editClub]
Author: Andrew Bocz
"""
import database
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
ident = form.getlist("ident")
name = form.getlist("name")
desc = form.getlist("desc")
pres = form.getlist("president")
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
'''.format("Saving Edit...")
if type(name[0]) != str or type(desc[0]) != str:
    print "<h1>Submit the Proper Data to Save</h1>"
    print "<p>Hit the back button to try again</p>"
    print "<p>{}</p>".format(type(name[0]))
elif len(name[0]) <= 1 or len(desc[0]) <= 1:
    print "<h1>Name and description must be filled out</h1>"
    print "<p>Hit the back button to try again</p>"
else:
    print "<h1>Editing {} club...</h1>".format(name[0])
    if pres:
        club =  (ident[0], name[0], desc[0], pres[0])
    else:
        club = (ident[0], name[0], desc[0], None)
    if grps:
        grps.insert(0, ident[0])
        database.updateGroups(grps)    
    database.updateClub(club)
    print "<a href=''>Edit another club</a>"
print '''
    </div>
    </body>
    </html>
'''
