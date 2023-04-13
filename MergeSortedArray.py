class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while nums2 != []:
            i = 0
            num = nums2.pop(0)
            while nums1[i] <= num and i < m:
                i += 1
            for j in range(len(nums1) - 1, i, -1):
                nums1[j] = nums1[j - 1]
            nums1[i] = num
            m += 1
