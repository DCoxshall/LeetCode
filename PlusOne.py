class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(i) for i in list(str(int(''.join([str(digits[i]) for i in range(len(digits))])) + 1))]
        # I did this on one line just to prove that I could.
        # Don't worry, I don't actually think this is a good way to write code.
