#!/usr/bin/python3
from collections import defaultdict, Counter

n = int(input())
graph = defaultdict(list)

for i in range(1, n + 1):
    immediate_manager = int(input())
    if immediate_manager != -1:
        graph[i].append(immediate_manager)

def depth_first_search(employee: int, level: int) -> None:
    visited.add(employee)

    for val in graph[employee]:
        if groups[val - 1] == groups[employee - 1] or groups[val - 1] != 0:
            groups[employee - 1] = groups[val - 1] + 1
        if val not in visited:
            depth_first_search(val, level + 1)

visited = set()
groups = [0 for i in range(n)]
for j in range(1, n + 1):
    if j not in visited:
        depth_first_search(j, 0)
print(len(Counter(groups)))
