#!/usr/bin/python3
""""""
from collections import defaultdict

def graphWithOutLongDirectedPaths() -> None:
    n, m = map(int, input().split())
    edges = defaultdict(int)

    i = 1
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        edges[(a, b)] = i
        i += 1


    def depth_first_search(node: int, alternate: int) -> bool:
        for neighbour in graph[node]:
            if color[neighbour - 1] == -1:
                color[neighbour - 1] = 1 - color[node - 1]
                rearranged[edges[(neighbour, node)] - 1] = alternate
                if not depth_first_search(neighbour, 1 - alternate):
                    return False
            if color[neighbour - 1] == color[node - 1]:
                return False
        return True
        # stack = [node]

        # while stack:
        #     val = stack.pop()

        #     for neighbour in graph[val]:
        #         if color[neighbour- 1] == -1:
        #             color[neighbour- 1] = 1 - color[val - 1]
        #             stack.append(neighbour- 1)
        #             rearranged[edges[(val, neighbour)] - 1] = alternate

        #         if color[neighbour- 1] == color[val - 1]:
        #             return False
        #     alternate = 1 - alternate
        # return True

    rearranged = [1 for _ in range(m)]
    color = [-1 for _ in range(n)]
    for i in range(1, n + 1):
        if color[i - 1] == -1:
            color[i - 1] = 0
            if not depth_first_search(i, 0):
                print('NO')
                break
    else:
        print('YES')
        print(''.join(str(j) for j in rearranged))



if __name__ == '__main__':
    graphWithOutLongDirectedPaths()
