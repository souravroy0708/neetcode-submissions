class Solution:
    def calPoints(self, operations: List[str]) -> int:

        st = []

        for index,op in enumerate(operations):
            print(f" op : {op} index : {index} st: {st}")
            if op == "+":
                new_val =int(st[-2])+int(st[-1])
                st.append(new_val)  
            elif op == "C":
                 st.pop()
            elif op == "D":
                new_val = int(st[-1]) *2
                st.append(new_val)
            else:
                st.append(op)
        
        res = 0
        for i in st:
            res +=int(i)
        
        return res
