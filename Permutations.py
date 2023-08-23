class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        perms = []
        for i in range(len(nums)):
            inner_perms = self.permute(nums[:i] + nums[i + 1:])
            for perm in inner_perms:
                perms.append([nums[i], *perm])
        return perms
