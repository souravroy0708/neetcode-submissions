class Solution:
    def trap(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        MaxLeft,MaxRight=height[left],height[right]

        res =0

        while left < right:
            print(" before left: {} right : {} MaxLeft : {} MaxRight:{}".format(left,right,MaxLeft,MaxRight))

            if height[left] < height[right]:
                left +=1
                MaxLeft = max(height[left],MaxLeft)
                print("Water Contain  left: {}".format(MaxLeft- height[left]))
                res += MaxLeft- height[left]
            else:
                right -=1
                MaxRight = max(height[right],MaxRight)
                print("Water Contain  right: {}".format(MaxRight- height[right]))
                res += MaxRight - height[right]
        return res

            