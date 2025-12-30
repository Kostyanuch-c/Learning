from collections import defaultdict


from collections import defaultdict


class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        graph = defaultdict(set)
        for a, b in connections:
            graph[a].add(b)
            graph[b].add(a)
        visited = set()
        result = 0
        stack = [0]
        directed = {(a, b) for a, b in connections}
        while stack:
            key = stack.pop()
            visited.add(key)
            for node in graph[key]:
                if node not in visited:
                    stack.append(node)
                    if (key, node) in directed:
                        result += 1
        return result

if __name__ == '__main__':
    solution = Solution()
    n = 5
    connections = [[1, 0], [1, 2], [3, 2], [3, 4]]
    print(solution.minReorder(n, connections))
