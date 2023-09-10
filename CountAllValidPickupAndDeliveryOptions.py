class Solution:
    def countOrders(self, n: int) -> int:
        if n == 1:
            return 1
        
        return int(self.countOrders(n - 1) * self.sumup(2 * (n-1) + 1)) % (10 ** 9 + 7)

    def sumup(self, n):
        return (n * (n + 1)) / 2
