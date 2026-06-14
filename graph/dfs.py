def dfs(node , adjacency_list, visited):
    visited.add(node)
    print(node)  # Process the node (e.g., print it)

    for neighbor in adjacency_list[node]:
        if neighbor not in visited:
            dfs(neighbor, adjacency_list, visited)

if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0],
        3: [1],
        4: [1]
    }

    visited = set()
    print("DFS starting from node 0:")
    dfs(0, graph, visited)