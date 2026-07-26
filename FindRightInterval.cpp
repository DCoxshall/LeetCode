typedef struct {
    int start;
    int orig_idx;
} Entry;

bool compare_entries(const Entry& a, const Entry& b) {
    return a.start < b.start;
}

class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        vector<int> answers;
        vector<Entry> entries = generateEntryVector(intervals);

        // For each interval, perform a binary search on the sorted list of
        // entries in order to find the entry with the closest start to this
        // interval's end.
        for (int i = 0; i < intervals.size(); i++) {
            int interval_end = intervals[i][1];
            answers.push_back(binarySearchForEntry(entries, interval_end));
        }

        return answers;
    }

    // Finds the entry e in entries such that e.start is as small as possible
    // while being greater than or equal to target. The return value is the 
    // original index in intervals of e, unless no such entry can be found, in
    // which case the return value is -1.
    int binarySearchForEntry(vector<Entry>& entries, int target) {
        int left = 0;
        int right = entries.size() - 1;

        while (left <= right) {
            int mid_idx = left + (right - left) / 2;
            int mid_val = entries[mid_idx].start;

            if (mid_val == target) {
                return entries[mid_idx].orig_idx;
            } else if (mid_val < target) {
                left = mid_idx + 1;
            } else {
                right = mid_idx - 1;
            }
        }

        // Items after `right` are greater than `target`, items before `left`
        // are less than `target`. Therefore, our value is the entry at index
        // `right + 1`, unless no such entry exists, in which case there is no
        // suitable entry in the list.
        if (right + 1 < entries.size()) {
            return entries[right+1].orig_idx;
        }
        return -1;
    }

    vector<Entry> generateEntryVector(vector<vector<int>>& intervals) {
        vector<Entry> entries;

        for (int i = 0; i < intervals.size(); i++) {
            Entry new_entry;
            new_entry.start = intervals[i][0];
            new_entry.orig_idx = i;
            entries.push_back(new_entry);
        }

        sort(entries.begin(), entries.end(), compare_entries);

        return entries;
    }
};
