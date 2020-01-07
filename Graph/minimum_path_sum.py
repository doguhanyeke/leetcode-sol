"""
 This question is a Dijkstra question
 I implemented the naive way, passed simple tests but got "time limit"
 will be reimplemented soon.
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        solutions = []
        rows = len(grid)
        cols = len(grid[0])

        # print(rows, cols)
        def dfs(visited, i, j):
            # print(i, j, visited)
            if i > rows - 1 and j > cols - 1:
                return
            if i == rows - 1 and j == cols - 1:
                solutions.append(visited)
                return
            if i < rows - 1:
                v = visited[:]
                v.append((i + 1, j))
                dfs(v[:], i + 1, j)
            if j < cols - 1:
                v = visited[:]
                v.append((i, j + 1))
                dfs(v[:], i, j + 1)

        dfs([], 0, 0)
        # print(solutions)
        path_min = sys.maxsize
        for path in solutions:
            tmp = 0
            for i in path:
                tmp += grid[i[0]][i[1]]
            # tmp += grid[rows-1][cols-1]
            tmp += grid[0][0]
            if tmp < path_min:
                path_min = tmp
        return path_min


"""
[[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],
 [9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],
 [8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],
 [6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],
 [7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],
 [9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],
 [1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],
 [3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],
 [1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],
 [5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],
 [2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],
 [0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
"""
