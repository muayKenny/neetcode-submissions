class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        # rows = words
        columns = []
        width = max(len(word) for word in words)

        for i in range(width):
            colWord = ""
            for word in words:
                if i < len(word):
                    colWord += word[i]
            columns.append(colWord)
        
        return columns == words

