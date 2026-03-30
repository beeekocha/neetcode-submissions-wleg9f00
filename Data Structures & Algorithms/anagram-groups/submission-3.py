class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict();

        for word in strs: 
            key = "".join(sorted(word))
            if key in anagrams: 
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
            print(anagrams[key])

        result = []

        for words in anagrams:
            result.append(anagrams[words])

        return result

