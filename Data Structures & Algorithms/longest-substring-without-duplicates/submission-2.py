class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longLen = 0
        l = 0
        r = 0
        curSet = set()

        while r < n:
            if s[r] in curSet:
                curSet.remove(s[l])
                l +=1
                continue
                
            else: curSet.add(s[r])

            curLen = len(curSet)
            if curLen > longLen:
                longLen = curLen

            r += 1

        return longLen

            