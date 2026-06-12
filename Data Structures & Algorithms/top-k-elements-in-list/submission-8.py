from collections import Counter,defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_count_of_numbers=Counter(nums)

        inverse_freq_hash=defaultdict(list)

        for val,freq in freq_count_of_numbers.items():
            inverse_freq_hash[freq].append(val)
        
        dummy_lst=[0]*(len(nums)+1)

        for freq,val in inverse_freq_hash.items():
            if dummy_lst[freq]!=0:
                dummy_lst[freq].extend(val)
            else:
                dummy_lst[freq]=val
        
        dummy_lst2=[]

        for val in range(len(dummy_lst)-1,-1,-1):
            if len(dummy_lst2)!=k:
                if dummy_lst[val]==0:
                    continue
                else:
                    dummy_lst2.extend(dummy_lst[val])
            else:
                return dummy_lst2
                
        
    
                

                


            

            

            





        