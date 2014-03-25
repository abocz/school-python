#
from Token import Token
import TokenType


class LexicalAnalyzer():

    def __init__(self, file_name):
        if not file_name:
            raise ValueError("Null file in LexicalAnalyzer")
        self.token_list = []
        line_num = 1
        holder = open(file_name)

    def processLine(self):
        assert 