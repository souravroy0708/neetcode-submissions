class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashdict = {}

        for index,element in enumerate(nums):
            print(f" index :  {index} : element : {element}")
            diff = target - element
            
            print(f" hashdict : {hashdict}")
            if diff in hashdict:
                return [hashdict.get(diff),index]
            
            hashdict[element] = index
        