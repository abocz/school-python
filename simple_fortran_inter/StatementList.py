class StatementList(object):
	# class level empty list
	def __init__(self):
		self.stmts = []
	# adds statement to the end of the list
	def add(self, statement):
		self.stmts.append(statement)
	# ?
	def execute(self):
		for x in range(len(self.stmts)):
			self.stmts[x].execute()