class Iterator:
    def __init__(self, items, start=0):
        self.list = items
        self.index = start
        self.previous = self.index - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.list):
            result = self.list[self.index]
            self.index += 1
            self.previous += 1
            return result
        else:
            result = self.list[self.previous]
            return result

    def __previous__(self):
        if self.previous > 0:
            self.index -= 1
            self.previous -= 1
            result = self.list[self.previous]
            return result
        else:
            result = self.list[self.previous]
            return result
