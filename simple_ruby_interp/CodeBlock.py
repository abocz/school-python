

class CodeBlock():
    #stmts = []
    def __init__(self):
        self.stmts = []

    def add(self, stmt):
        if not stmt:
            raise ValueError("Null Statement argument in Codeblock")
        self.stmts.append(stmt)

    def execute(self):
        for s in self.stmts:
            s.execute()