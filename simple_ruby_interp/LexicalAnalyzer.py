#
from LexicalException import LexicalException
from Token import Token
from TokenType import TokenType


class LexicalAnalyzer(object):

    def __init__(self, file_name):
        if not file_name:
            raise ValueError("Null file in LexicalAnalyzer")
        self.token_list = []
        line_num = 1
        input = open(file_name)
        lines = [line.strip() for line in input]
        #warning we need a different solution here
        while line_num < len(lines)+1:
            self.process_line(lines[line_num-1], line_num)
            line_num += 1
        input.close()
        eosToken = Token("EOS", line_num, 1, TokenType.TokenType.EOS_TOK)
        self.token_list.append(eosToken)

    def process_line(self, line, line_num):
        assert line is not None
        assert line_num > 0
        column_num = 0
        column_num = self.skip_white_space(line, column_num)
        while column_num < len(line):
            lexeme = self.get_lexeme(line, column_num)
            type = self.determine_token_type(lexeme, line_num, column_num)
            tok = Token(line_num, column_num+1, lexeme, type)
            self.token_list.append(tok)
            column_num += len(lexeme)
            column_num = self.skip_white_space(line, column_num)

    def determine_token_type(self, lexeme, line_num, column_num):
        assert lexeme is not None
        assert line_num > 0
        assert column_num >= 0
        if lexeme[0].isalpha():
            if len(lexeme) is 1:
                tokType = TokenType.ID_TOK
            elif lexeme == "if":
                tokType = TokenType.IF_TOK
            elif lexeme == "until":
                tokType = TokenType.UNTIL_TOK
            elif lexeme == "then":
                tokType = TokenType.THEN_TOK
            elif lexeme == "else":
                tokType = TokenType.ELSE_TOK
            elif lexeme == "end":
                tokType = TokenType.END_TOK
            elif lexeme == "puts":
                tokType = TokenType.PUTS_TOK
            elif lexeme == "def":
                tokType = TokenType.DEF_TOK
            elif lexeme == "while":
                tokType = TokenType.WHILE_TOK
            elif lexeme == "do":
                tokType = TokenType.DO_TOK
            else:
                raise LexicalException("Invalid lexeme", line_num, column_num)
        elif lexeme[0].isdigit():
            if self.all_digits(lexeme):
                tokType = TokenType.LIT_INT
        elif lexeme == "=":
            tokType = TokenType.ASSIGN_OP
        elif lexeme == "+":
            tokType = TokenType.ADD_TOK
        elif lexeme == "-":
            tokType = TokenType.SUB_TOK
        elif lexeme == "*":
            tokType = TokenType.MUL_TOK
        elif lexeme == "/":
            tokType = TokenType.DIV_TOK
        elif lexeme == "==":
            tokType = TokenType.EQ_TOK
        elif lexeme == "/=":
            tokType = TokenType.NE_TOK
        elif lexeme == "<":
            tokType = TokenType.LT_TOK
        elif lexeme == "<=":
            tokType = TokenType.LE_TOK
        elif lexeme == ">":
            tokType = TokenType.GT_TOK
        elif lexeme == ">=":
            tokType = TokenType.GE_TOK
        else:
            raise LexicalException("Invalid lexeme", line_num, column_num)
        return tokType

    def all_digits(self, s):
        assert s is not None
        i = 0
        while (i < (len(s))) and (s[i].isdigit()):
            i += 1
        return i == len(s)

    def get_lexeme(self, line, column_num):
        assert line is not None
        assert column_num >= 0
        i = column_num
        while (i < len(line)) and (not line[i].isspace()):
            i +=1
        return line[i:i]

    def skip_white_space(self, line, column_num):
        assert line is not None
        assert column_num >= 0
        while (column_num < len(line)) and (line[column_num].isspace()):
            column_num += 1
        return column_num

    def get_next_token(self):
        if not self.more_tokens():
            raise LexicalException("No more tokens")
        return self.token_list.pop(0)

    def more_tokens(self):
        return not self.token_list

    def get_lookahead_token(self):
        if not self.more_tokens():
            raise LexicalException("No more tokens")
        return self.token_list[0]









