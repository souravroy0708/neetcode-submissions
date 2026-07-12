class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i))+'#'+i
            #print(f" i : {i} res : {res}")
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            #print(f" i : {i}")
            j = i + 1 

            while s[j] != '#':
                j +=1

            length = int(s[i:j])

            #print(f" i : {i} j : {j} length : {length}")

            s_out = s[j+1:j+1+length]

            #print(f"s : {s_out}")

            res.append(s_out)

            i =j+1+length

            #print(f"next i index : {i} res : {res}")

        return res

