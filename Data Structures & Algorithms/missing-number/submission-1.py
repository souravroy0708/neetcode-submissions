class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=len(nums)

        for i in range(len(nums)):

            res +=i-nums[i]

            print(" i : nums[i] : res : ".format(i,nums[i], res))
        return res
        