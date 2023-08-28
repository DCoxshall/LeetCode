class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        arr = [[999 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]

        # Initialise edges
        for i in range(len(obstacleGrid)):
            arr[i][0] = 1
        for j in range(len(obstacleGrid[0])):
            arr[0][j] = 1

        # Place stones
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    arr[i][j] = 0

        # Alter edges
        for i in range(len(obstacleGrid)):
            if arr[i][0] == 0:
                for k in range(i, len(obstacleGrid)):
                    arr[k][0] = 0
                break
            else:
                pass

        for j in range(len(obstacleGrid[0])):
            if arr[0][j] == 0:
                for l in range(j, len(obstacleGrid[0])):
                    arr[0][l] = 0
                break
            else:
                pass

        print(arr)

        # Do calculation
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if arr[i][j] == 0:
                    pass
                else:
                    arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
        
        return arr[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]
