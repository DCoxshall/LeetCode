from math import factorial

class Solution:
    def __init__(self):
        self.memo = {}

    def generate(self, numRows: int) -> list[list[int]]:
        return [self.generateN(n) for n in range(0, numRows)]

    def generateN(self, n: int) -> list[int]:
        row = []
        for r in range(n + 1):
            row.append(int(self.myfactorial(n)/(self.myfactorial(r) * self.myfactorial(n - r))))
        return row

    def myfactorial(self, n: int):
        if n not in self.memo:
            self.memo[n] = factorial(n)
        return self.memo[n]
