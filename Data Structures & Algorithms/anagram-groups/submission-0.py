class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = {}

        for str in strs:
            code = [0] * 26
            for char in str:
                code[ord(char) - ord('a')] += 1
            code = tuple(code)
            if code not in anaDict:
                anaDict[code] = [str]
            else: 
                anaDict[code].append(str)

        returnList = list(anaDict.values())
        return returnList 