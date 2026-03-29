class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # constraints
        # nums - is a list of digits, we always have nums and len < 10^4
        # k - is always persist and > 0

        #Approach 1:
        num_dict = dict();

        # O(N)
        for num in nums: 
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        
        buckets = [[] for i in range(len(nums) + 1)]

        for num in num_dict:
            buckets[num_dict[num]].append(num)

        print(buckets, 'buck')
        result = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)   
                if len(result) == k:
                    return result
            
