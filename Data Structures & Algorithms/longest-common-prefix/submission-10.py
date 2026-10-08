class Solution:
    def longestCommonPrefix(self, strs: List[s]) -> s:
        if not strs[0]:
            return ""
        prefix = strs[0]
        for i, s in enumerate(strs[1:]):
            if not s:
                prefix = ""
            if len(s) < len(prefix):
                prefix = prefix[:len(s)]
            for j in range(len(s)):
                if j >= len(prefix):
                    break
                if s[j] != prefix[j]:
                    prefix = prefix[:j]
                    


        return prefix
