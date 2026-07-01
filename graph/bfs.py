def bfs(node, adjacency_list, visited):
    queue = [node]
    bfs_order = []

    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            visited.add(current_node)
            bfs_order.append(current_node)
            queue.extend(adjacency_list[current_node])

    return bfs_order
        

# Example graph represented as an adjacency list
graph = {
    0: [1, 2],
    1: [0,4],
    2: [0],
    3: [4],
    4: [1,3]
}

visited = set()
print("BFS starting from node 0:")
bfs_result = bfs(0, graph, visited)
print(bfs_result)
