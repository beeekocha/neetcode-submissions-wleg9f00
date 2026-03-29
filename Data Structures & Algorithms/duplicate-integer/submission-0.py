class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # define a dictionary to store charachters and their count
        char_dict = dict() 
        # either can do this with Counter
        # char_dict = Counter(nums);
        for i in nums:
            if i in char_dict:
                return True
            else:
                char_dict[i] = 1;

        return False 
   