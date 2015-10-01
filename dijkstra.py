def dijkstra(graph, source):
    dist = {}; prev = {}; path = {}
    Q = []
    
    for k in graph:
        dist[k] = float('inf')
        prev[k] = None
        Q.append(k)
    dist[source] = 0
    
    while Q:
        min_dist = float('inf')
        min_node = None
        
        for node in Q:
            if dist[node] < min_dist:
                min_dist = dist[node]
                min_node = node
        Q.remove(min_node)
        
        for neighbor in graph[min_node]:
            alt = dist[min_node] + graph[min_node][neighbor] 
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = min_node
                
    for k in graph:
        parent = prev[k]
        p = [k]
        while parent:
            p.append(parent)
            parent = prev[parent]
        path[k] = p[::-1]
        
    return {'dist':dist, 'path':path}

if __name__ == "__main__":
    graph = {'s': {'a': 2, 'b': 1},
            'a': {'s': 3, 'b': 4, 'c':8},
            'b': {'s': 4, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 7, 't': 4},
            'd': {'b': 1, 'c': 11, 't': 5},
            't': {'c': 3, 'd': 5}}
    result = dijkstra(graph, 's')
    
    print("source node: 's'")
    print("shortest paths:")
    for node in result['path']:
        print(node + " (cost=" + str(result['dist'][node]) + "): " + str(result['path'][node]))
