class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasmap=set()
        for element in nums:
            if element in hasmap:
                return True
            hasmap.add(element)
        return False
        