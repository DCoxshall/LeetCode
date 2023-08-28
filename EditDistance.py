# AKA Levenshtein Distance

class Solution:
    def __init__(self):
        self.memo = {}

    def minDistance(self, word1: str, word2: str) -> int:
        if (word1, word2) in self.memo:
            return self.memo[(word1, word2)]
        if len(word1) == 0:
            self.memo[(word1, word2)] = len(word2)
            return len(word2)
        if len(word2) == 0:
            self.memo[(word1, word2)] = len(word1)
            return len(word1)
        if word1[0] == word2[0]:
            self.memo[(word1, word2)] = self.minDistance(word1[1:], word2[1:])
            return self.memo[(word1, word2)]
        else:
            possibilities = [self.minDistance(word1[1:], word2), self.minDistance(word1, word2[1:]), self.minDistance(word1[1:], word2[1:])]
            self.memo[(word1, word2)] = 1 + min(possibilities)
            return 1 + min(possibilities)
