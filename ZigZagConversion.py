class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for i in range(numRows)]
        cur = 0
        descending = True
        for i in s:
            rows[cur].append(i)
            if descending == False:
                cur -= 1
            else:
                cur += 1

            if cur == numRows:
                descending = False
                cur = numRows - 2
            if cur < 0:
                descending = True
                cur = 1

        ans = ""
        for i in rows:
            ans += ''.join(i)
        return ans
