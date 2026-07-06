class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right=0,len(heights)-1

        max_water=0
        while left<right:
            print("left : {} right : {}".format(left,right))
            current_water=min(heights[left],heights[right])*(right-left)
            max_water = max(max_water,current_water)

            if heights[left]<heights[right]:
                left +=1
            else:
                right -=1
            print("final max water : {} left : {} right: {}".format(max_water,left,right))
        return max_water

        