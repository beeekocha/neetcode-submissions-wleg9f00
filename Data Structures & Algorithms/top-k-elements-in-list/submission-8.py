class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_freq = dict()

        for num in nums:
            if num in k_freq:
                k_freq[num] += 1
            else:
                k_freq[num] = 1

        buckets = [[] for i in range(len(nums) + 1)]

        for num, counts in k_freq.items():
            buckets[counts].append(num)

        result = []
        
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
            
        






        