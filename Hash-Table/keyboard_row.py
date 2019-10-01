class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        str1 = "qwertyuiop"
        str2 = "asdfghjkl"
        str3 = "zxcvbnm"
        rows = [str1, str2, str3]

        lst = list(map(lambda x: x.lower(), words))
        result = []

        for ind, ele in enumerate(lst):
            for row in rows:
                if all(c in row for c in ele):
                    result.append(ind)
                    break
        return [words[i] for i in result]
