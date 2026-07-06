class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open={")":"(","}":"{","]":"["}
        stack = []

        for element in s:
            if element in close_to_open:
                if stack and stack[-1]==close_to_open.get(element):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(element)

            print(" element : {} -stack : {}".format(element,stack))
        return True if not stack else False


        