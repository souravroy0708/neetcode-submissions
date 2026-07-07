class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = defaultdict(list)

        for str in strs:
            count = [0]*26

            for s in str:
                count[ord(s) - ord('a')] +=1
            res_dict[tuple(count)].append(str)
        print(f"res_dict : {res_dict}")
        res = res_dict.values
        return list(res_dict.values())