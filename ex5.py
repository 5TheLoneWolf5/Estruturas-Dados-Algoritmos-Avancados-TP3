cidades = {
    'Cruzamento A': [("Cruzamento B", 4), ("Cruzamento C", 7)],
    'Cruzamento B': [("Cruzamento A", 12), ("Cruzamento C", 8), ("Cruzamento D", 5)],
    'Cruzamento C': [("Cruzamento A", 3), ("Cruzamento B", 5), ("Cruzamento D", 1)],
    'Cruzamento D': [("Cruzamento B", 5), ("Cruzamento C", 3)],
}

def dijkstra(graph, start, goal):
    shortest_distance = {}
    track_predecessor = {}
    unseenNodes = dict(graph)
    infinity = float('inf')
    track_path = []

    for node in unseenNodes:
        shortest_distance[node] = infinity

    shortest_distance[start] = 0

    while unseenNodes:
        min_distance_node = None

        for node in unseenNodes:
            if min_distance_node is None or shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node

        if min_distance_node is None:
            break 

        for child_node, weight in graph[min_distance_node]:
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node

        unseenNodes.pop(min_distance_node)

    currentNode = goal
    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]
        except KeyError:
            return
    track_path.insert(0, start)

    if shortest_distance[goal] != infinity:
        print('Distância mais curta: ' + str(shortest_distance[goal]))
        print('Caminho é: ' + str(track_path))
    else:
        print("Caminho não foi encontrado.")

dijkstra(cidades, 'Cruzamento A', 'Cruzamento D')