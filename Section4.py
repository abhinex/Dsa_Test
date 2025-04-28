## Section 4: Graphs
# 7. Shortest Path in an Unweighted Graph:
# Given an undirected graph and a source node, implement **Breadth-First Search (BFS)** to find the shortest path to all other nodes.

def bfs_shortest_path(graph, start):
    # Initialize a distance dictionary to store shortest distance to each node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Distance to the start node is 0
    
    # Initialize a queue for BFS using a simple list
    queue = [start]
    
    # Perform BFS
    while queue:
        node = queue.pop(0)  # Get the front element from the queue (using pop(0))
        
        
        for neighbor in graph[node]:
            if distances[neighbor] == float('inf'):  
                distances[neighbor] = distances[node] + 1  # Update distance
                queue.append(neighbor)  
    
    return distances

# Example 
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

start_node = 0
result = bfs_shortest_path(graph, start_node)

print("Shortest distances from node", start_node, ":", result)

# output: Shortest distances from node 0 : {0: 0, 1: 1, 2: 1, 3: 2}


# 8. Detect Cycle in a Directed Graph:
# Implement an algorithm to detect a cycle in a directed graph using **DFS**

def detect_cycle(graph):
    visited = {node: 0 for node in graph}  
    
    def dfs(node):
        # If the node is in the recursion stack, a cycle is detected
        if visited[node] == 1:
            return True
        
        # If the node has been fully processed, no need to visit again
        if visited[node] == 2:
            return False
        
        
        visited[node] = 1
        
        for neighbor in graph[node]:
            if dfs(neighbor):  
                return True
        
        
        visited[node] = 2
        return False
    
    # Check for cycles in each node
    for node in graph:
        if visited[node] == 0:  
            if dfs(node):  # If a cycle is detected during DFS traversal
                return True
    
    return False

# Example 
graph = {
    0: [1],
    1: [2],
    2: [0],
    3: [4],
    4: []
}

if detect_cycle(graph):
    print("Cycle detected in the graph.")
else:
    print("No cycle detected in the graph.")
