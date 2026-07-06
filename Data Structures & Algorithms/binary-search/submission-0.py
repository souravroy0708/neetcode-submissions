class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res=-1
        for index,element in enumerate(nums):
            if element==target:
                return index
        return res

        