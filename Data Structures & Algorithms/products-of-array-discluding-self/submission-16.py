class Solution:
    def productExceptSelf(self, c: List[int]) -> List[int]:

        res=[1]*len(c)

        prefix=1

        for index in range(len(c)):
            print("index",index)
            res[index] = prefix
            prefix=prefix*c[index]
           
        print("res",res)
        #[1,1,2,8]

        postfix=1

        for index_post in range((len(c)-1),-1,-1):
            print("postfix index_post",index_post)
            res[index_post] *= postfix
            postfix *= c[index_post]

        #[24,12,4,1]
        
        return res