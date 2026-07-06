class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq={}
        
        for num in nums:
            num_freq[num]=num_freq.get(num,0)+1
            
        num_freq_group=[[] for i in range(len(nums)+1)]
        print("num_freq",num_freq)
        print("num_freq_group",num_freq_group)

        for num,freq in  num_freq.items():
            print("num: {} freq: {}".format(num,freq))
            num_freq_group[freq].append(num)

        print("num_freq_group-----ggg",num_freq_group) 

        res=[]
        for element in  num_freq_group[::-1]:
            print("element",element)
            if  element and len(res)<k:
                res.extend(element) 
        return res  