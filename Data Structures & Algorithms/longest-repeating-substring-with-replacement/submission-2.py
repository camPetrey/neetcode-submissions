class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        long = 0
        charSet = set(s)


        for char in charSet:
            count = 0
            left = 0

            #count unique char
            for right in range(len(s)):
                if s[right] == char:
                    count += 1

                #Make window valid
                while right - left + 1 - count > k:
                    if s[left] == char:
                        count -= 1
                    left += 1

                #Update long for valid window
                long = max(long, right - left + 1)

        return long