class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i+1
            right = len(nums)-1

            while left < right:
                res = nums[left] + nums[right] + nums[i]

                if res == 0:
                    result.append([nums[i], nums[left], nums[right]]);
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                   
                
                if res > 0:
                    right -= 1
                
                if res < 0:
                    left += 1;
        
        return result

