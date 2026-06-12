from collections import deque

def topological_sort_bfs(graph):
    
    indegree = {}
    
    for node in graph:
        indegree[node] = 0
    
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1
    
    queue = deque()
    
    for node in indegree:
        if indegree[node] == 0:
            queue.append(node)
    
    topo_order = []
    
    while queue:
        current = queue.popleft()
        topo_order.append(current)
        
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return topo_order


def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': ['E'],
        'E': []
    }
    
    order = topological_sort_bfs(graph)
    
    print("Topological Order using BFS:")
    print(" -> ".join(order))


if __name__ == "__main__":
    main()