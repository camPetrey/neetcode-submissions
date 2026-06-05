class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long = 0
        l = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            long = max(long, len(seen))

        return long

            


