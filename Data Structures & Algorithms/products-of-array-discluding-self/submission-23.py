class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1]*len(nums)
        print(f" res : {res}")

        prefix = 1
        for i in range(len(nums)):
            print(f"i : {i} prefix : {prefix}")
            res[i]=prefix
            prefix = prefix * nums[i]
        print(f" res : {res}")

        postfix = 1

        for j in range(len(nums)-1,-1,-1):
            print(f"j :{j} postfix : {postfix}")
            res[j] = res[j] * postfix
            postfix = postfix *nums[j]

        return res 
