from LexicalException import LexException
from Parser import Parser
from ParserException import ParserException
from Program import Program


class Interpreter(object):

    def main():
        try:
            p = Parser("test1.rb")
            progs = Program(p.parse())
            progs.execute()
        except LexException as e:
            print(e)
        except ParserException as e:
            print(e)
        except ValueError as e:
            print(e)
            print("ValueError from Interpreter")
        except Exception as e:
            print(e)
            print("Unknown error occurred - terminating")

    if __name__ == "__main__":
        main()

