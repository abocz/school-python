class StatementList(object):
	# class level empty list
	stmts = []
	#def __init__(self):
	#	self.stmts = []

	def add(self, statement):
		self.stmts.append(statement)

	def execute(self):
		for x in range(len(self.stmts)):
			self.stmts[x].execute()