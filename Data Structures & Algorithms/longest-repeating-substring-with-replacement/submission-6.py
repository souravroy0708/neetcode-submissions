class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left=0
        
        char_freq = {}
        max_length = 0
        for right in range(len(s)):
            char_freq[s[right]] = char_freq.get(s[right],0)+1

            print(f" left : {left} right : {right} char_freq : {char_freq}")

             

            while right-left+1 - max(char_freq.values()) > k:
                print(f" inside condition break left : {left} right : {right} char_freq : {char_freq}")
                char_freq[s[left]] -=1
                left += 1

            print(f" max_length : {max_length} cur_length : {right-left+1}")
            max_length = max(max_length,right-left+1)
            

        return max_length
            




