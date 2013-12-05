#!/usr/bin/python
"""
Assignment06 Dist Systems CS4520
Second part of editing a new club
selectClubForEdit -> [editSelectClub] -> editClub
Author: Andrew Bocz
"""
import database
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
ident = int(form.getfirst("chosen",))
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
'''.format("Edit Selected Club")
club = database.getClubById(ident)
print "<h1>Edit {} Club</h1>".format(club[1])
editForm = '''
<form method='get'>
<div class='data-grid'>
<div>
<span><p>Id:</p></span>
<span><input type='text' name='ident' size='12' value='{0[0]}' readonly></span>
<span></span>
</div>
<div>
<span><p>Name:</p></span>
<span><input type='text' name='name' size='12' value='{0[1]}'></span>
<span></span>
</div>
<div>
<span><p>Description:</p></span>
<span><input type='text' name='desc' size='30'value='{0[2]}'></span>
</div>
</div>
'''
print editForm.format(club)
president = database.getPersonById(club[3])
members = list(database.getPersonByClub(club[0]))
if members:		
	print '''
	<h3>Choose the Club President</h3>
	<p>The current president, if there is one, it is pre-selected</p>
	<select name='president'>
	'''
	if president:
		print "<option value='{}'>{}</options>".format(president[0], president[1])
		members.remove((president[0],))
	for member in members:
		memberHolder = database.getPersonById(member[0])
		print "<option value='{}'>{}</option>".format(memberHolder[0], memberHolder[1])
	print "</select>"
else:
	print "<h3>Currently No members</h3>"

print '''
<h3>Select Groups</h3>
'''
groups = list(database.getListOfGroups())
currentGroups = database.getGroupByClub(club[0])
if currentGroups:
	for curGroup in currentGroups:
		curGroupHolder = database.getGroupById(curGroup[0])
		print "<input type='checkbox' value={0[0]} name='groups' checked>{0[1]}<br />".format(curGroupHolder)
		groups.remove(curGroupHolder)
	for group in groups:
		groupHolder = database.getGroupById(group[0])
		print "<input type='checkbox' value={0[0]} name='groups'>{0[1]}<br />".format(groupHolder)
else:
	for group in groups:
		groupHolder = database.getGroupById(group[0])
		print "<input type='checkbox' value={0[0]} name='groups'>{0[1]}<br />".format(groupHolder)
print '''
<p>
<input type='submit' value='Save Changes' formaction='editClub.py'/>
<button formaction='selectClubForEdit.py' formmethod='post'>Cancel</button>
</p>
</form>
</div>
</body>
</html>
'''
