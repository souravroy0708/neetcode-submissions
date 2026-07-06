class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res=[0]*length
        prefix=[0]*length
        postfix=[0]*length

        prefix[0]=postfix[length-1]=1

        print("res ",res)
        print("prefix",prefix)
        print("postfix",postfix)

        for i in range(1,length):
            print(i)
            prefix[i] = prefix[i-1] * nums[i-1]
        
        print("prefix final ",prefix)
        
        for i in range (length-2,-1,-1):
            print(i)
            postfix[i] = postfix[i+1] * nums[i+1]

        print("postfix",postfix)

        for i in range(length):
            res[i] = prefix[i] *postfix[i]

        return res
        