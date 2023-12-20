class Solution:
    def isValid(self, s: str) -> bool:
        dict_s = {"(": ")", "{": "}", "[": "]"}
        list_s = []
        for i, specific_s in enumerate(s):
            if len(list_s) == 0 or dict_s.get(list_s[-1]) != specific_s:
                list_s.append(specific_s)
            else:
                list_s.pop()
        return len(list_s) == 0
