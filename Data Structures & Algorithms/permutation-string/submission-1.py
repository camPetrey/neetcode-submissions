class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        map1 = {}
        window = {}
        left = right = 0

        for char in s1:
            map1[char] = map1.get(char, 0) + 1

        while right < len(s2):
            window[s2[right]] = window.get(s2[right], 0) + 1

            while right - left + 1 > len(s1):
                window[s2[left]] = window[s2[left]] - 1
                if window[s2[left]] == 0:
                    window.pop(s2[left])
                left += 1

            if window == map1:
                return True
            right += 1

        return False
            


        