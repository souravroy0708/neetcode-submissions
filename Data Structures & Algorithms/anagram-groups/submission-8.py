class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group_anagram_dict=defaultdict(list)
        print("group_anagram_dict",group_anagram_dict)

        for word in strs:
            counter=[0]*26
            for char in word:
                counter[ord(char)-ord("a")] += 1

            print("word",word)
            print("counter",counter)
            group_anagram_dict[tuple(counter)].append(word)

        print("group_anagram_dict",group_anagram_dict)

        return list(group_anagram_dict.values())
