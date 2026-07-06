class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        count = defaultdict(list)
        print(f"count : {count}")
        for word in strs:
            innner_dict = [0]*26
            print(f"inner_dict : {innner_dict}")
            for char in word:
                innner_dict[ord(char)-ord('a')] +=1
            count[tuple(innner_dict)].append(word)
        
        print(f"count : {count}")
    
        return list(count.values())