#Note: Should be working, concerned with execute method very similar to UntilStatement
from Statement import Statement


class WhileStatement(Statement):
    """
    WhileStatement statement object has BooleanExpression expr and CodeBlack cblock
    """
    def __init__(self, expr, cblock):
        if not expr:
            raise ValueError("Invalid or null expression argument in WhileStatement")
        if not cblock:
            raise ValueError("Invalid or null code block argument in WhileStatement")
        self.expr = expr
        self.cblock = cblock

    def execute(self):
        while self.expr.evaluate():
            self.cblock.execute()
