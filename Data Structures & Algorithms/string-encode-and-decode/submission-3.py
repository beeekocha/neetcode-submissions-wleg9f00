class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        result = ""
        for s in strs:
            result = result + str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        result = []
        i = 0

        while i < len(s):
            temp = ""

            while s[i] != "#":
                temp += s[i]
                i += 1

            length = int(temp)
            i += 1

            result.append(s[i:i + length])
            i += length

        return result


