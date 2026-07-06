class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hasset=set(nums)

        longest_seq = 0

        for num in nums:
            
            current_seq=1
            if num-1 not in hasset:
                print(" num seq start: {} current_seq: {}".format(num,current_seq))
                while num+current_seq in hasset:
                    current_seq +=1
            
            longest_seq = max(longest_seq,current_seq)
            print(" num after current seq final : {} longest_seq: {}".format(num,longest_seq))
        return longest_seq

        