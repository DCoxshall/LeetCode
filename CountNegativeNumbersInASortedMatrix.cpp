class Solution {
   public:
    int countNegatives(vector<vector<int>> &grid) {
        int total = 0;
        for (int i = 0; i < grid.size(); i++) {
            int row_count = countNegativesInRow(grid[i]);
            total += row_count;
        }
        return total;
    }

    // Counts the number of negatives in the given row.
    int countNegativesInRow(vector<int> &row) {
        int neg_idx = binarySearch(row);
        return row.size() - neg_idx;
    }

    // Finds the index of the first negative number in the row. If there are no
    // negative numbers in the row, return the size of the row.
    int binarySearch(vector<int> &row) {
        // Every value before `left` is greater than 0.
        // Every value after `right` is less than 0.
        int left = 0;
        int row_len = row.size();
        int right = row_len - 1;

        while (left <= right) {
            int mid_idx = left + (right - left) / 2;
            int mid_val = row[mid_idx];

            // If the value we've found is greater than zero, we want to search
            // to the right, because the array is non-increasing.
            if (mid_val > 0) {
                left = mid_idx + 1;
            }

            // Likewise, if the value we've found is less than zero, we want to
            // search to the left.
            else if (mid_val < 0) {
                right = mid_idx - 1;
            }

            // Additionally, if we've found zero, we scan to the right to find
            // the index of the first negative value.
            else if (mid_val == 0) {
                int i = mid_idx;

                while (i < row_len && row[i] == 0) {
                    i++;
                }

                return i;
            }
        }

        // If we don't find zero in the row, we just return the `right + 1`,
        // because every value after `right` is STILL less than zero.
        // Therefore, `right + 1` is the location of the first negative number,
        // or the location at which the first negative number would be
        // inserted.
        return right + 1;
    }
};
