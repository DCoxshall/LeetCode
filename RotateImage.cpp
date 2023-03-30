#include <algorithm>
#include <vector>

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        // Tranpose matrix
        for (int i = 0; i < matrix[0].size(); i++) {
            for (int j = i + 1; j < matrix[0].size(); j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            } 
        }

        // Reverse each row in the matrix
        for (int i = 0; i < matrix[0].size(); i++) {
            std::reverse(matrix[i].begin(), matrix[i].end());
        }
    }
};
