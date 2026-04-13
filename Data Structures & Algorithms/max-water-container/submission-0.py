class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if heights == None or len(heights) == 0:
            return 0
        
        left = 0;
        right = len(heights)-1;
        maximum = 0;
        
        while left < right:
            min_h = min(heights[left], heights[right])
            area = min_h * (right - left)
            if (area > maximum):
                maximum = area
            if heights[left] >= heights[right]:
                right -=1;
            else:
                left +=1;
        
        return maximum
        