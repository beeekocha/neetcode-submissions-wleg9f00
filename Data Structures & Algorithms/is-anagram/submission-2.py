class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # SECOND APPROACH: 
        # edge case where we don't have s or t
        if s is None or t is None:
            return False
        
        # edge case where the s and t are not equil size
        if len(s) != len(t):
            return False
        
        return True if sorted(s) == sorted(t) else False


        # FIRST APPROACH -> T: O(N) AND S: O(N)
        # # edge case where we don't have s or t
        # if s is None or t is None:
        #     return False
        
        # # edge case where the s and t are not equil size
        # if len(s) != len(t):
        #     return False

        # # simple task with a dictionary
        # s_dict = dict()
        # # also can be used Counter here
        # # s_dict = Counter(s)

        # for char in s:
        #     if char in s_dict:
        #         s_dict[char] += 1
        #     else:
        #         s_dict[char] = 1
        
        # # checking validity of t in s[dict]
        # # what if we have "rac" and "rcc"
        # # r in dict and > 0-> d[r] = 0; contin
        # # c in dict and > 0-> d[c] = 0; contin
        # # c in dict BUT = 0-> FALSE
        # # Going out and return True value
        # # m Not in dict -> FALSE

        # for char in t:
        #     if char in s_dict and s_dict[char] > 0:
        #         s_dict[char] -= 1;
        #     else:
        #         return False
        
        # return True
