class Solution:
    def isPalindrome(self, s: str) -> bool:
        #bruteForse

        new_string=""
        for char in s:
            if char.isalnum():
               new_string = new_string +char.lower()

        print("new_string : {}".format(new_string))

        reverse_string = new_string[::-1]
        print("reverse_string : {}".format(reverse_string))

        res=False
        if new_string == reverse_string:
            res=True

        return res
        