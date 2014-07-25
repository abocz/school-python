#!/usr/bin/python
"""
Assignment06 Dist Systems CS4520
First part of entering a new club
[enterNewClub] -> newClub -> saveClub
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
'''.format("Enter new club")

print "<h1>Enter Data for a New Club:</h1>"

print '''
<form method='get'>
<div class='data-grid'>
<div>
<span>Name:</span>
<span><input type='text' size='12' name='name'></span>
</div>
<div>
<span><p>Description:</p></span>
<span><input type='text' size='30' name='description'></span>
</div>
</div>
'''

print "<h2>Select Groups:</h2>"
groups = database.getListOfGroups()
for group in groups:
    print "<input type='checkbox' value={0[0]} name='groups'>{0[1]}<br />".format(group)

print '''
<p>
<input type='submit' value='Save New Club' formaction='saveClub.py'/>
<button formaction='enterClub.py' formmethod='post'>Cancel</button>
</p>
</form>
</div>
</body>
</html>
'''

