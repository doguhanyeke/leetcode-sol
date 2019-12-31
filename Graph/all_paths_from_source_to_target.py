class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        visited = []
        result = []
        last_node = len(graph) - 1

        def dfs(visited, graph, node, mylist):
            if node not in visited:
                mylist.append(node)
                if node == last_node:
                    result.append(mylist)

                    return
                visited.append(node)
                for neighbour in graph[node]:
                    # print(neighbour, mylist)
                    dfs(visited[:], graph, neighbour, mylist[:])

        dfs(visited, graph, 0, [])
        return result