class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(0, n + 1):
            total = 0
            while i > 0:
                if i & 1 == 1:
                    total += 1
                i >>= 1
            ans.append(total)
        return ans
