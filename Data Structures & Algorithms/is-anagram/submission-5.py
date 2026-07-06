class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq={}
        t_freq={}

        if len(s) != len(t):
            return False

        for index in range(0,len(s)):
            s_freq[s[index]] = s_freq.get(s[index],0)+1
            t_freq[t[index]] = t_freq.get(t[index],0)+1
        
        print("SSS",s_freq)
        print("TTTTT",t_freq)

        for elemet in s:
            if s_freq.get(elemet) !=  t_freq.get(elemet,0):
                return False
        return True