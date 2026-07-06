class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort

        count = {}

        freq = [ [] for i in range(len(nums)+1)]

        print(f" freq : {freq}")

        for i in nums:
            count[i] = 1+ count.get(i,0)

        print(f"count : {count}")

        res = []

        for key,val in count.items():
            freq[val].append(key)

        print(f"freq : {freq}")

        for i in range(len(freq)-1,0,-1):
            for el in freq[i]:
                res.append(el)
                if len(res) == k:
                    print(f"inside res : {res} i : {i} K : {k}")
                    return res
        
        return res