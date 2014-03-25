#
from BooleanExpression import BooleanExpression
from CodeBlock import CodeBlock
from LexicalAnalyzer import LexicalAnalyzer
from ParserException import ParserException
from Program import Program
from TokenType import TokenType
from UntilStatement import UntilStatement
import WhileStatement


class Parser():

    def __init__(self, file_name):
        assert file_name
        self.lex = LexicalAnalyzer(file_name)

    def parse(self):
        tok = self.get_next_token()
        self.match(tok, TokenType.DEF_TOK)
        cb = self.get_codeblock()
        tok = self.get_next_token()
        self.match(tok, TokenType.END_TOK)
        tok = self.get_next_token()
        if tok.get_token_type() != TokenType.EOS_TOK:
            raise ParserException("Garbage at end of program")
        return Program(cb)

    def get_codeblock(self):
        cd = CodeBlock()
        stmt = self.get_statement()
        cd.add(stmt)
        tok = self.get_lookahead_token()
        while self.is_valid_start_of_statement(tok):
            stmt = self.get_statement()
            cd.add(stmt)
            tok = self.get_lookahead_token()
        return cd

    def is_valid_start_of_statement(self, tok):
        assert tok
        return (tok.getTokenType() == TokenType.ID_TOK) or (tok.getTokenType() == TokenType.IF_TOK) or (tok.getTokenType() == TokenType.WHILE_TOK) or (tok.getTokenType() == TokenType.UNTIL_TOK) or (tok.getTokenType() == TokenType.PUTS_TOK)

    def get_statement(self):
        tok = self.get_lookahead_token()
        if tok.get_token_type() == TokenType.ID_TOK:
            stmt = self.get_assignment_statement()
        elif tok.get_token_type() == TokenType.IF_TOK:
            stmt = self.get_if_statement()
        elif tok.get_token_type() == TokenType.PUTS_TOK:
            stmt = self.get_print_statement()
        elif tok.get_token_type() == TokenType.UNTIL_TOK:
            stmt = self.get_until_statement()
        elif tok.get_token_type() == TokenType.WHILE_TOK:
            stmt = self.get_while_statement()
        else:
            raise ParserException("Statement expected", tok.get_row_number(), tok.get_column_number)
        return stmt

    def get_while_statement(self):
        tok = self.get_next_token()
        self.match(tok, TokenType.WHILE_TOK)
        expr = self.get_boolean_expression()
        tok = self.get_next_token()
        self.match(tok, TokenType.DO_TOK)
        cb = self.get_codeblock()
        tok = self.get_next_token()
        self.match(tok, TokenType.END_TOK)
        return WhileStatement(expr, cb)

    def get_until_statement(self):
        tok = self.get_next_token()
        self.match(tok, TokenType.WHILE_TOK)
        expr = self.get_boolean_expression()
        tok = self.get_next_token()
        self.match(tok, TokenType.DO_TOK)
        cb = self.get_codeblock()
        tok = self.get_next_token()
        self.match(tok, TokenType.END_TOK)
        return UntilStatement(expr, cb)

    def get_if_statement(self):
        pass

    def get_print_statement(self):
        pass

    def get_assignment_statement(self):
        pass

    def get_expression(self):
        pass

    def get_arithmetic_operatir(self):
        pass

    def get_boolean_expression(self):
        pass

    def get_relational_operator(self):
        pass

    def match(self, tok, tokType):
        pass

    def get_next_token(self):
        pass

    def get_lookahead_token(self):
        pass