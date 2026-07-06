class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for index,element in enumerate(s):
            #print(f"index : {index} element : {element}")
            s_dict[s[index]] = s_dict.get(s[index],0)+1
            t_dict[t[index]] = t_dict.get(t[index],0)+1
        
        #print(f"s_dict : {s_dict} t_dict: {t_dict}")

        for key,val in s_dict.items():
            #print(f" key: {key} val : {val} t val : {t_dict.get(key,0)}")

            if val != t_dict.get(key,0):
                return False
        
        return True


        