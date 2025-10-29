class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        il = 0
        ir = len(matrix)

        # Canonical binary search: lower bound is inclusive, upper bound is exclusive.
        # The midpoint is equal to the integer division of the sum of the upper and lower bounds.
        # That way, we'll always have the "perfect" midpoint - either the exact middle (in the case
        # of odd-numbered arrays) or the first of the center two (in the case of even-numbered arrays).
        # Doing this means we can set either the upper or the lower bound exactly to the midpoint.

        while ir > il + 1:
            mid = (il + ir) // 2
            if target < matrix[mid][0]:
                ir = mid
            else:
                il = mid
        
        jl = 0
        jr = len(matrix[0])

        while jr > jl + 1:
            mid = (jl + jr) // 2
            if target < matrix[il][mid]:
                jr = mid
            else:
                jl = mid
        
        return matrix[il][jl] == target
