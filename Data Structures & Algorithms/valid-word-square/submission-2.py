class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        colWidth = max(len(word) for word in words)
        columns = []
        for i in range(colWidth):
            # for every column, iterate through every word, and grab the 
            # letter in the current column.
            colWord = ""
            for word in words:
                if i < len(word):
                    colWord += word[i]
            columns.append(colWord)

        return columns == words