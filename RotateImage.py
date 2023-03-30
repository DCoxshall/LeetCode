class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        for row in matrix:
            row.reverse()
        return matrix

    def transpose(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix[0])):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in matrix:
            for j in i:
                print(j, end=" ")
            print()
        return matrix
