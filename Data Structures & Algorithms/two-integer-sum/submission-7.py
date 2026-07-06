class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map_dict = {}
        for index,i in enumerate(nums):
            print(f" index : {index} i : {i}")
            missing = target-i
            if missing in map_dict:
                return [map_dict[missing],index]
            map_dict[i]=index