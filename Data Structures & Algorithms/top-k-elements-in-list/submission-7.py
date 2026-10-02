class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freakMap = {}
        for i in nums:
            if i in freakMap:
                freakMap[i] += 1
            else:
                freakMap[i] = 1

        output = sorted(freakMap,key=lambda x: freakMap[x], reverse=True)
        return output[:k]
