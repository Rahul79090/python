def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    visited.add(start)
    parent = {start: None}  

    while stack:
        node = stack.pop()
        if node == goal:
         
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]  
          
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                stack.append(neighbor)

    return None 

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
goal = 'F'

dfs_result = dfs(graph, start, goal)
print("DFS path:", dfs_result)

