def errorPage(*messages):
	print "<h2>There has been an error</h2>"	
	if len(messages) == 0:
		pass
	elif len(messages) == 1:
		print "<p>{}</p>".format(messages[0])
	else:
		print "<ul>"
		for message in messages:
			print "<li>{}</li>".format(message)
		print "</ul>"
