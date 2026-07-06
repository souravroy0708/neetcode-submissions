class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        max_len = 0
        numsset = set(nums)

        for i in nums:
            print(f"i :{i}")

            if i-1 not in numsset:
                current_len = 0
                start = i
                print(f" current len : {current_len} i : {i}")
                
                while start in numsset:
                    current_len +=1
                    start +=1 

                max_len = max(current_len,max_len)

                print(f"i : {i} current_len : {current_len} max_len : {max_len}")
        
        return max_len
