

class StatementSequence():
	
	def __init__(self):
		self.stmnts = []
		
	def add(self, stmnt):
		if not stmnt:
			raise ValueError("Expected statement in StSeq")
		self.stmnts.append(stmnt)
		
	def execute(self):
		for s in self.stmnts:
			s.execute()