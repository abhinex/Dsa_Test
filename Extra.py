def dijkstra_with_list(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    unvisited_nodes = list(graph.keys())

    while unvisited_nodes:
        # Find the node with the smallest distance
        current_node = min(unvisited_nodes, key=lambda node: distances[node])
        unvisited_nodes.remove(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances
graph = {
    'A': {'B': 1, 'C': 4},  # A -> B: 1, A -> C: 4
    'B': {'A': 1, 'C': 2, 'D': 5},  # B -> A: 1, B -> C: 2, B -> D: 5
    'C': {'A': 4, 'B': 2, 'D': 1},  # C -> A: 4, C -> B: 2, C -> D: 1
    'D': {'B': 5, 'C': 1}  # D -> B: 5, D -> C: 1
}

# Call the function with the graph and start node 'A'
print(dijkstra_with_list(graph, 'A'))