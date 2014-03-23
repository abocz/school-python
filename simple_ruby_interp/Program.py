#


class Program():

    def __init__(self, cblock):
        if not cblock:
            raise ValueError("Code Block Error in Prorgam")
        self.cblock = cblock

    def execute(self):
        self.cblock.execute()

