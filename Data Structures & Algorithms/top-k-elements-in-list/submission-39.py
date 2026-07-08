class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num,0)+1

        buckets = [[] for i in range(len(nums)+1)]
        print(f"buckets empty: {buckets}")
        for num,freq in freq_dict.items():
            print(f"num : {num} freq : {freq}")
            buckets[freq].append(num)
        print(f"buckets final: {buckets}")
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            print(f" i : {i}")
            for num in buckets[i]:
                print (f"num : {num}")
                res.append(num)
                if len(res) == k:
                    return res
        
        return res