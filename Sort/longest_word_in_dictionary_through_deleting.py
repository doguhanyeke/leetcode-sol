from typing import List
from collections import OrderedDict


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (-len(x), x), reverse=True)
        for cand in d[::-1]:
            ind = 0
            for i in cand:
                found_index = s[ind:].find(i)
                ind += found_index
                if found_index != -1:
                    ind += 1
                    continue
                else:
                    ind = len(s) + 2
                    break
            if ind <= len(s):
                return cand
        return ""


if __name__ == '__main__':
    s = Solution()
    d = ["apple", "ewaf", "awefawfwaf", "awef", "awefe", "ewafeffewafewf"]
    print(s.findLongestWord("aewfafwafjlwajflwajflwafj", d))


