from LexException import LexException
from Token import Token
from TokenType import TokenType


class LexicalAnalyzer(object):
	def __init__(self, fileName):
		if fileName is None:
			raise ValueError("null argument")
		self.tokenList = []
		lineNum = 1
		input = open(fileName)
		lines = [line.strip() for line in input]
		while lineNum < len(lines)+1:
			self.processLine(lines[lineNum-1], lineNum)
			lineNum += 1
		eosToken = Token("EOS",lineNum,1, TokenType.EOS_TOK)
		self.tokenList.append(eosToken)
		input.close()
	def processLine(self, line, lineNum):
		assert line is not None
		index = 0
		index = self.skip_white_space(line, index)
		while index < len(line):
			lexeme = self.getLexeme(line, index, lineNum)
			tokType = self.getTokenType(lexeme, lineNum, index)
			tokenHolder = Token(lexeme, lineNum, index+1, tokType)
			self.tokenList.append(tokenHolder)
			index += len(lexeme)
			index = self.skip_white_space(line, index)
	def getTokenType(self, lexeme, lineNum, columnNum):
		assert lexeme is not None
		assert len(lexeme) > 0
		assert lineNum >= 1
		#assert columnNum >= 1
		lexeme.lower()
		#print the lexeme
		print(lexeme)
		if lexeme[0].isalpha():
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
		elif lexeme[0].isdigit():
			i = 0
			while (i < (len(lexeme))) and (lexeme[i].isdigit()):
				i += 1
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
		return line[index:i]
	def skip_white_space(self, line, index):
		assert line is not None
		assert index >= 0
		while (index < len(line)) and (line[index].isspace()):
			index += 1
		return index
	def getNextToken(self):
		if not self.tokenList:
			raise ValueError("no more tokens")
		return self.tokenList.pop(0)
	def getLookaheadToken(self):
		if not self.tokenList:
			raise ValueError("no more tokens")
		return self.tokenList[0]