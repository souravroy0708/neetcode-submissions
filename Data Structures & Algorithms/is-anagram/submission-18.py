class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_char_freq = {}
        t_char_freq = {}

        for i in range(len(s)):
            s_char_freq[s[i]] = s_char_freq.get(s[i],0) +1
            t_char_freq[t[i]] = t_char_freq.get(t[i],0) +1
        
        print(f" {s} : {s_char_freq} ")
        print(f" {t} : {t_char_freq} ")

        for key,val in s_char_freq.items():
            if t_char_freq.get(key) != val:
                return False
        
        return True

        