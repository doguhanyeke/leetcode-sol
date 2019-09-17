class Solution(object):
    mydict = {0: 0, 1: 1, 2: 1}

    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.mydict:
            return self.mydict[n]
        result = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        self.mydict[n] = result
        return result
