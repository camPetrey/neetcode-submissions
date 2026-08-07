class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")":"(", "]":"[", "}":"{"}
        stack = []

        for char in s:
            if char in "({[":
                stack.append(char)

            else:
                if not stack or stack.pop() != hashmap[char]:
                    return False

        return len(stack) == 0
