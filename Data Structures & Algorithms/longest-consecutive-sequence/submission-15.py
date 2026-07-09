class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)

        res={}
        max_counter = 0
        for num in nums:
            inner_res = [num]
            counter = 1
            if num-1 not in nums_set:
                
                while num+counter in nums_set:
                    inner_res.append(num+counter)
                    #print(f"num : {num} counter : {counter} inner_res : {inner_res}")
                    counter +=1
                    
            max_counter = max(max_counter,counter)
            res[num] = inner_res
        #print(f" res : {res} ")
        return max_counter

        