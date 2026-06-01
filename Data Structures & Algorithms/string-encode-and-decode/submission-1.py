class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string))+"#"+string

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            wordLen = int(s[i:j])
            j += 1

            word = s[j : j+wordLen]
            decoded.append(word)

            i = j + wordLen

        return decoded