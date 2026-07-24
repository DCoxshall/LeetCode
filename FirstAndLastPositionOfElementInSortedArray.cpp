class Solution {
   public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;

        int target_idx = -1;

        while (left <= right) {
            int mid_idx = left + (right - left) / 2;
            int mid_val = nums[mid_idx];

            if (mid_val < target) {
                left = mid_idx + 1;
            } else if (mid_val > target) {
                right = mid_idx - 1;
            } else if (mid_val == target) {
                return scanForRange(nums, mid_idx);
            }
        }

        return vector<int>{-1, -1};
    }

    vector<int> scanForRange(vector<int>& nums, int idx) {
        int val = nums[idx];
        int l = idx;
        int r = idx;

        while (l > 0 && nums[l] == val) l--;

        while (r < nums.size() - 1 && nums[r] == val) r++;

        if (nums[l] != val) l++;

        if (nums[r] != val) r--;

        return vector<int>{l, r};
    }
};
