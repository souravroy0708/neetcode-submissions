class Solution:
    def isValid(self, s: str) -> bool:

        #valid_dict = {"(":")","{":"}","[":"]"}
        valid_dict = {")":"(","}":"{","]":"["}

        res = []

        for char in s:
            print(f"char : {char}")
            if char in valid_dict.values():
                res.append(char)
                print(f"after append char : {char} res : {res}")
            elif len(res) > 0 and char in valid_dict.keys():
                print(f"inside remove char : {char} res : {res} deleted char : {valid_dict.get(char,"NA")}")
                #if valid_dict.get(char,"NA") in res:
                if res[-1] == valid_dict.get(char,"NA"):
                    res.pop()
                    print(f"after remove char : {char} res : {res} deleted char : {valid_dict[char]}")
                else:
                    return False
            elif len(res) == 0 and char in valid_dict.keys():
                print(f"after detected invalid: {char} res : {res}")
                return False
        
        if len(res) == 0:
            return True
        else:
            return False


