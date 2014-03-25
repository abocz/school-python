#


class Memory(object):
    mem = [0] * 52

    def fetch(self, var):
        assert var
        return self.mem[self.get_index(var)]

    def store(self, var, value):
        assert var
        assert value
        self.mem[self.get_index(var.] = value

    def get_index(self, ch):
        assert ch
        if ch[0].isupper():
            index = ord(ch) - ord('A')
        else:
            index = ord(ch) - ord('a') + ord('26')
        return index