class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     prevMap={}

     for index,element in  enumerate(nums):
        print("element {} index {}".format(element,index))
        diff=target-element
        if diff in prevMap:
            return [prevMap.get(diff),index]
        else:
            prevMap[element]=index
    