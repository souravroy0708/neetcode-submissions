class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_seen=set()
        for element in nums:
            if element in has_seen:
                return True
            has_seen.add(element)
        return False
        