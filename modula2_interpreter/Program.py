

class Program():

	def __init__(self, ss):
		if not ss:
			raise ValueError("StatementSequence invalid in Program")
		self.ss = ss
	
	def execute(self):
		self.ss.execute()