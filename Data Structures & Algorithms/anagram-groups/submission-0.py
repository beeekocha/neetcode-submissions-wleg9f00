class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count_char=[0]*26
            for char in s:
                count_char[ord(char) - ord('a')] += 1
            result[tuple(count_char)].append(s)
        return list(result.values())


        