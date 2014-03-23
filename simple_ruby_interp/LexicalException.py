
class LexicalException(Exception):
    def __init__(self, message, line_num, column_num):
        if not message:
            raise ValueError("null string argument")
        if line_num <= 0:
            raise ValueError("invalid line argument")
        if column_num <= 0:
            raise ValueError("invalid column argument")
        self.message = message
        self.line_num = line_num
        self.column_num = column_num

    def __str__(self):
        return "{} at line number {} column number {}".format(self.message, self.line_num, self.column_num)
