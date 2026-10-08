class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i, str in enumerate(strs[1:]):
            if not str:
                prefix = ""
            if len(str) < len(prefix):
                prefix = prefix[:len(str)]
            for j in range(len(str)):
                if j >= len(prefix):
                    break
                if str[j] != prefix[j]:
                    prefix = prefix[:j]
                    


        return prefix
