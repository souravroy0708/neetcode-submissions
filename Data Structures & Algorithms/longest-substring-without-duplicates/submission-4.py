class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_char_set=set()
        left = 0
        res = 0
        for right in range(len(s)):
            print("left : {} right : {}".format(left,right))

            while s[right] in unique_char_set:
                
                unique_char_set.remove(s[left])
                left +=1
            unique_char_set.add(s[right])
            

            res = max(res,right-left+1)


            #right +=1
        
        return res

            

        