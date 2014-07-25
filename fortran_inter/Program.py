class Program(object):

	def __init__(self, sList):
		if sList is None:
			raise ValueError("null list argument")
		print("slist print")
		self.sList = sList

	def execute(self):
		self.sList.execute()