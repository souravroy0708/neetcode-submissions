class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sdict = {}
        tdict = {}

        for index in range(0,len(s)):
            sdict[s[index]] = sdict.get(s[index],0)+1
            tdict[t[index]] = tdict.get(t[index],0)+1
        
        print("sdict - {}".format(sdict))
        print("tdict - {}".format(tdict))

        for key,value in sdict.items():
            print ("key - {}".format(key))
            if sdict.get(key,0) != tdict.get(key,0):
                return False
        
        return True
        