class Program(object):

	def __init__(self, sList):
		# check for null list
		if sList is None:
			raise ValueError("null list argument")
		self.sList = sList

	def execute(self):
		self.sList.execute()