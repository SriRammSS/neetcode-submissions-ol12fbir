class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        new_list=set(nums)
        length=1
        longest_seq=0

        for i in new_list:
            if i-1 not in new_list:
                
                check_number=i+1
                while check_number in new_list:
                    length=length+1
                    check_number=check_number+1
            longest_seq=max(longest_seq,length)
        
        return longest_seq


        

        