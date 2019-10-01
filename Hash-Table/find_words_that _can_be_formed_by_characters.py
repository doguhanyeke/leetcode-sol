from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        size = 0
        c_chars = Counter(chars)
        for word in words:
            c_word = Counter(word)
            if all(k in c_chars and c_chars[k] >= c_word[k] for k in c_word.keys()):
                size += len(word)
        return size
