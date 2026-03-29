class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramdict = dict();

        for word in strs:
            sorted_chars = sorted(word)
            key = "".join(sorted_chars)
  
            if key in anagramdict:
                anagramdict[key].append(word)
            else:
                anagramdict[key] = [word]
            
        result = []

        for res in anagramdict:
            result.append(anagramdict[res])

        return result
        