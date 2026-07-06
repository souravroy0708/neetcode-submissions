class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map={}

        for index,element in enumerate(nums):
            diff=target-element
            if diff in diff_map:
                return [diff_map.get(diff),index]
            else:
                  diff_map[element]=  index
                