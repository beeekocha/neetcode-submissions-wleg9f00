class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = dict();

        for i in nums:
            print(i)
            if i in seen:
                return True;
            else:
                seen[i] = 1;
        
        return False;

