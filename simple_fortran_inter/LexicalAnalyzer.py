from LexException import LexException
from Token import Token
from TokenType import TokenType


class LexicalAnalyzer(object):
	def __init__(self, fileName):
		if fileName is None:
			raise ValueError("null argument")
		self.tokenList = []
		lineNum = 1
		#open file
		eosToken = Token("EOS",lineNum,1, TokenType.EOS_TOK)
		self.tokenList.append(eosToken)
		print(self.tokenList[0].getLexeme())
		input = open(fileName)
		#read lines into list, may misplace cursor, may be unneeded
		lines = [line.strip() for line in input]
		#apply processLine to each line iterating through the file
		while lineNum < len(lines):
			print("line:"+str(lineNum))
			self.processLine(lines[lineNum-1], lineNum)
		#create eos token
		eosToken = Token("EOS",lineNum,1, TokenType.EOS_TOK)
		self.tokenList.append(eosToken)
		input.close()
	def processLine(self, line, lineNum):
		assert line is not None
		index = 0
		index = self.skip_white_space(line, index)
		while index < len(line):
			print("started while"+str(lineNum))
			lexeme = self.getLexeme(line, index, lineNum)
			print(lexeme)
			tokType = self.getTokenType(lexeme, lineNum, index)
			print("tok type")
			print(tokType)
			tokenHolder = Token(lexeme, lineNum, index+1, tokType)
			print("tok holder")
			print(tokenHolder)
			self.tokenList.append(tokenHolder)
			print(len(lexeme))
			index = index + len(lexeme)
			print("index:"+str(index))
			index = self.skip_white_space(line, index)
			print("finished while:"+str(lineNum))
	def getTokenType(self, lexeme, lineNum, columnNum):
		print("begin token")
		assert lexeme is not None
		assert len(lexeme) > 0
		assert lineNum >= 1
		print(str(columnNum))
		#assert columnNum >= 1
		#token work
		tokType = TokenType.EOS_TOK
		lexeme.lower()
		if lexeme[0].isalpha:
			if len(lexeme) is 1:
				tokType = TokenType.ID_TOK
			else:
				if lexeme == "program":
					tokType = TokenType.PROGRAM_TOK
				elif lexeme == "end":
					tokType = TokenType.END_TOK
				elif lexeme == "if":
					tokType = TokenType.IF_TOK
				elif lexeme == "then":
					tokType = TokenType.THEN_TOK
				elif lexeme == "else":
					tokType = TokenType.ELSE_TOK
				elif lexeme == "do":
					tokType = TokenType.DO_TOK
				elif lexeme == "write":
					tokType = TokenType.WRITE_TOK
				else:
					raise LexException("invalid lexeme", lineNum, columnNum)
		elif lexeme[0].isdigit:
			i = 0
			while i < (len(lexeme)) and (lexeme[i].isdigit):
				i = i + 1
			if i == len(lexeme):
				tokType = TokenType.INT_TOK
			else:
				raise LexException("invalid integer constant", lineNum, columnNum)
		else:
			if lexeme == "(":
				tokType = TokenType.LEFT_PAREN_TOK
			elif lexeme == ")":
				tokType = TokenType.RIGHT_PAREN_TOK
			elif lexeme == "=":
				tokType = TokenType.ASSIGNMENT_TOK
			elif lexeme == "<=":
				tokType = TokenType.LE_TOK
			elif lexeme == "<":
				tokType = TokenType.LT_TOK
			elif lexeme == ">=":
				tokType = TokenType.GE_TOK
			elif lexeme == ">":
				tokType = TokenType.GT_TOK
			elif lexeme == "==":
				tokType = TokenType.EQ_TOK
			elif lexeme == "/=":
				tokType = TokenType.NE_TOK
			elif lexeme == "+":
				tokType = TokenType.ADD_TOK
			elif lexeme == "-":
				tokType = TokenType.SUB_TOK
			elif lexeme == "*":
				tokType = TokenType.MUL_TOK
			elif lexeme == "/":
				tokType = TokenType.DIV_TOK
			elif lexeme == ",":
				tokType = TokenType.COMMA_TOK
			else:
				raise LexException("invalid lexeme", lineNum, columnNum)
		return tokType
	def getLexeme(self, line, index, lineNum):
		assert line is not None
		assert index >= 0
		assert lineNum > 0
		i = index
		while (i < len(line)) and (not line[i].isspace()):
			i += 1
		# ensure slicing is done correctly here
		return line[index:i]
		# ensure slicing
	def skip_white_space(self, line, index):
		assert line is not None
		assert index >= 0
		print("we made it here")
		while (index < len(line)) and (line[index].isspace()):
			index += 1
			print("oh well, what about this?")
		return index
	def getNextToken(self):
		if not self.tokenList:
			raise ValueError("no more tokens")
		return self.tokenList.pop([0])
	def getLookaheadToken(self):
		if not self.tokenList:
			raise ValueError("no more tokens")
		return self.tokenList[0]