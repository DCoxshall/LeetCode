class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        index1 = len(nums) - 2
        while index1 > -1:
            if nums[index1] < nums[index1 + 1]:
                break
            else:
                index1 -= 1

        if index1 == -1:
            nums.reverse()
            return

        index2 = len(nums) - 1
        while index2 > -1:
            if nums[index2] > nums[index1]:
                break
            else:
                index2 -= 1
        nums[index1], nums[index2] = nums[index2], nums[index1]
        nums[index1 + 1:] = sorted(nums[index1 + 1:])
