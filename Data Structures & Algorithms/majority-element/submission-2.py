class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = {}

        for i in nums:
            count[i] = count.get(i,0)+1
        
        print(f" count : {count}")

        
        for key,val in count.items():
            if val >= len(nums)/2:
                return key




        