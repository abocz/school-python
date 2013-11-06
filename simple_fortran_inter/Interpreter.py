from LexException import LexException
from Parser import Parser
from ParserException import ParserException
from Program import Program


class Interpreter(object):
	#run the program with a try catch block
	def main():
		try:
			p = Parser("test3.for")
			prog = Program(p.parse())
			prog.execute()
		except LexException as e:
			print(e)
		except ParserException as e:
			print(e)
		except ValueError as e:
			print(e)
		except Exception as e:
			print(e)
			print("Unknown error occurred - terminating")
	if __name__ == "__main__":
		main()