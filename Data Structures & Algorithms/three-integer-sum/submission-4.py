class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    
                    sum_res=nums[i]+nums[j]+nums[k]
                    print("I : {} J : {} : K: {} sum_res: {}".format(i,j,k,sum_res))
                    if sum_res==0:
                        match_array=[nums[i],nums[j],nums[k]]
                        match_array.sort()
                        if match_array not in res:
                            res.append(match_array) 
        return res

        