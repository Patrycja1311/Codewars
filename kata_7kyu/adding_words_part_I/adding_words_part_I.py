class Arith():
    def __init__(self, value):
        self.words = [
            "zero", "one", "two", "three", "four", "five",
            "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen", "twenty"
        ]
        self.value = value

    def add(self, other):
        a = self.words.index(self.value)
        b = self.words.index(other)
        return self.words[a + b]
