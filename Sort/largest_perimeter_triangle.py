class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        print(A[0])
        for i in range(len(A)):
            if A[i+1] + A[i+2] > A[i]:
                return sum(A[i:i+3])
            if i == len(A)-3:
                return 0
