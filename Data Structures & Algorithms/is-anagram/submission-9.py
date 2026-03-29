class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if s == None or t == None:
            return False

        if len(s) != len(t):
            return False

        # Solution 1: sorting
        # sortedS = "".join(sorted(s)) O(n)
        # sortedT = "".join(sorted(t)) O(n)

        # if (sortedS == sortedT):
        #     return True
        # return False

        # Solution 2: dict
        seenS = dict()

        for char in s:
            if char in seenS:
                seenS[char] += 1;
            else:
                seenS[char] = 1;

        for char in t:
            if char not in seenS:
                return False
            
            seenS[char] -= 1;
            
            if seenS[char] >= 0:
                continue
            
            return False
        
        return True
            





       

