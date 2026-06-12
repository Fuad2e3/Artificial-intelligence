def dfs(node, graph, visited, stack):
    visited.add(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited, stack)
    
    stack.append(node)


def topological_sort(graph):
    visited = set()
    stack = []
    
    for node in graph:
        if node not in visited:
            dfs(node, graph, visited, stack)
    
    return stack[::-1]


def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': ['E'],
        'E': []
    }
    
    order = topological_sort(graph)
    
    print("Topological Order:")
    print(" -> ".join(order))


if __name__ == "__main__":
    main()