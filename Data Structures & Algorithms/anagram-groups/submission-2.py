class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            count = [0] * 26 
            for char in word:
                count[ord(char) - ord('a')] +=1
            hashmap[tuple(count)].append(word)
        
        return list(hashmap.values())
        # Result with sorted string
        # anagramdict = dict();

        # for word in strs:
        #     sorted_chars = sorted(word)
        #     key = "".join(sorted_chars)
  
        #     if key in anagramdict:
        #         anagramdict[key].append(word)
        #     else:
        #         anagramdict[key] = [word]
            
        # result = []

        # for res in anagramdict:
        #     result.append(anagramdict[res])

        # return result
        