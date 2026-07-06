class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq={}
        t_freq={}

        if len(s) != len(t):
            return False

        for index,elemnet in enumerate(s):
            s_element=s[index]
            t_element=t[index]

            s_freq[s_element]=s_freq.get(s_element,0)+1
            t_freq[t_element]=t_freq.get(t_element,0)+1
        
        print(s_freq)
        print(t_freq)

        for char in s:
            if s_freq.get(char,0) != t_freq.get(char,0):
                return False
        return True
        