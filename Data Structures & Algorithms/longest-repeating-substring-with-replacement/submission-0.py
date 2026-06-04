class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        long = 0
        chars = set(s)

        for char in chars:
            count = 0
            left = 0

            for right in range(len(s)):
                if s[right] == char:
                    count += 1

                while (right - left + 1) - count > k:
                    if s[left] == char:
                        count -= 1
                    left += 1

                long = max(long, right - left +1)
        return long

