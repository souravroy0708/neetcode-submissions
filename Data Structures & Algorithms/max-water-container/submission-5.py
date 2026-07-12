class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left=0
        right = len(heights)-1
        max_water = 0

        while left<right:
            store_water = (right - left) * min(heights[left] , heights[right])

            print(f" left : {left} right : {right} left_val : {heights[left]} right_val : {heights[right]} store_water : {store_water}")
            max_water = max(max_water,store_water)

            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        
        return max_water



