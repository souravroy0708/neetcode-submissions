class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hasset= set(nums)
        longest=0
        for num in nums:
            print("num 1st : {}".format(num))
            if (num-1) not in hasset:
                current_streak=1
                while (num+current_streak) in hasset:
                    current_streak +=1
                longest=max(longest,current_streak)
                print("num : {} current_streak : {}".format(num,current_streak))
        return longest