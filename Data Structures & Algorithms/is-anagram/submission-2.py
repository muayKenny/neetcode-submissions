class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        for letter in s:
            if letter in countS:
                countS[letter] += 1
            else:
                countS[letter] = 1


        for letter in t:
            if letter in countS:
                countS[letter] -= 1
            else:
                return False

        for count in countS.values():
            if count != 0:
                return False

        return True