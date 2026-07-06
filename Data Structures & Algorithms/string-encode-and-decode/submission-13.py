class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""

        for word in strs:
            res += str(len(word))+'#'+word
        
        print("encode res : {}".format(res) )
        return res

    def decode(self, s: str) -> List[str]:

        res=[]

        start=0
        # 4#neet4#co d  e  4  #  l  o  v  e  3  #  y  o  u
        # 0123456789 10 11 12 13 14 15 16 17 18 19 20 21 22
        while start<len(s) :
            end=start
            while s[end] !="#":
                end +=1

            print("before length start : {} end : {}".format(start,end))
            length=int(s[start:end])
    
            start = end+1
            end=length+start
             
            

            word = s[start:end]
            
            print("final  start :{} end : {} word: {}".format(start,end,word))
            res.append(word)
            start=end
        
        return res



