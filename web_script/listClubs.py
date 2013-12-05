#!/usr/bin/python
"""
Assignment06 Dist Systems CS4520
Lists all of the clubs
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
'''.format("List of Clubs")

print "<h1>List of Clubs</h1>"
clubs = database.getListOfClubs()
print "<ul>"
for club in clubs:
    print "<li>{}</li>".format(club[1])
    print "<ul>"
    print "<li>Ident: {}</li>".format(club[0])
    print "<li>Description: {}</li>".format(club[2])
    pres = database.getPersonById(club[3])
    if pres:
        print "<li>President: {}</li>".format(pres[1])
    else:
        print "<li>President: None</li>"
    print "<li>Club has these members:</li>"
    print "<ul>"
    persons = database.getPersonByClub(club[0])
    if persons:
        for person in persons:
            name = database.getPersonById(person[0])
            print "<li>{}</li>".format(name[1])
    else:
        print "<li>No members</li>"
    print "</ul>"
    print "<li>Club belongs to this group:</li>"
    print "<ul>"
    groups = database.getGroupByClub(club[0])
    if groups:
        for group in groups:
            name = database.getGroupById(group[0])
            print "<li>{}</li>".format(name[1])
    else:
        print "<li>No groups</li>"
    print "</ul>"
    print "</ul>"
print "</ul>"
print '''
</div>
</body>
</html>
'''
