class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i == len(arr) -1:
                arr[i] = -1
            else: 
                current = arr[i+1]
                for j in range(i + 1, len(arr)):
                    if current < arr[j]:
                        current = arr[j]
                arr[i] = current
                current = 0
        
        return arr