class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.generate(res, "", 0, 0, n)
        return res

    def generate(self, res, s, _open, _close, n):
        if _open == n and _close == n:
            res.append(s)
            return
        
        if _open < n:
            self.generate(res, s + '(', _open + 1, _close, n)
            
        if _close < _open:
            self.generate(res, s + ')', _open, _close + 1, n)
