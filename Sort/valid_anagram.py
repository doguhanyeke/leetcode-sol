import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_elements, t_elements = map(collections.Counter, (s, t))
        if len(s_elements) != len(t_elements):
            return False
        for i in s_elements:
            if i not in t_elements:
                return False
            if s_elements[i] != t_elements[i]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))
