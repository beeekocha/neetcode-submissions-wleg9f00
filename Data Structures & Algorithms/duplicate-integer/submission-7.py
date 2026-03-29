class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenDictionary = dict()

        for num in nums:
            if num in seenDictionary:
                return True;
            else:
                seenDictionary[num] = 1        
        return False;