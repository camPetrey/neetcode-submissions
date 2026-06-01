class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}

        if(len(s) != len(t)):
            return False

        for i in range(len(s)):
            sMap[s[i]] = sMap.get(s[i], 0) + 1
            tMap[t[i]] = tMap.get(t[i], 0) + 1

        for char in s:
            if sMap.get(char, 0) != tMap.get(char, 0):
                return False

        return True