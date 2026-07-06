class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res=[0]*n
        prefix_res =[0]*n
        suffix_res = [0]*n

        prefix_res[0]=suffix_res[n-1]=1

        for index in range(1,n):
            print("prefix index :{}".format(index))
            prefix_res[index]= prefix_res[index-1]*nums[index-1]
        
        print("prefix_res",prefix_res)
        #[1,1,2,8]

        for index in range((n-2),-1,-1):
            print("suffix_res index :{}".format(index))
            
            suffix_res[index] = suffix_res[index+1] * nums[index+1]

        print(suffix_res)
        #[48,24,6,1]

        for i in range(n):
           res[i] = prefix_res[i] *suffix_res[i]
        return res
        