#Note to self: believed to be correct and complete


class Token(object):
    """
    Token object has int row_number, int column_number, string lexeme, and TokenType type
    """

    def __init__(self, row_number, column_number, lexeme, tok_type):
        if row_number <= 0:
            raise ValueError("Invalid row number from Token")
        if column_number <= 0:
            raise ValueError("Invalid column number from Token")
        if lexeme is None or 0:
            raise ValueError("Invalid lexeme from Token")
        self.row_number = row_number
        self.column_number = column_number
        self.lexeme = lexeme
        self.tok_type = tok_type

    def get_token_type(self):
        return self.tok_type

    def get_column_number(self):
        return self.column_number

    def get_row_number(self):
        return self.row_number

    def get_lexeme(self):
        return self.lexeme