def bfs(graph, start) -> set:
    queue = []
    queue.append(start)
    visited = set()

    while queue:
        vertex = queue.pop(0)
        if vertex in visited:
            continue
        visited.add(vertex)
        for neighbor in graph[vertex]:
            queue.append(neighbor)

    return visited


def check_gas_supply(cities, gas_storages, pipelines):
    graph = {}
    result = []

    for city in cities:
        graph[city] = []
    for gas_storage in gas_storages:
        graph[gas_storage] = []
    for origin, destination in pipelines:
        graph[origin].append(destination)

    for gas_storage in gas_storages:
        reachable_cities = bfs(graph, gas_storage)
        unreachable_cities = []
        for city in cities:
            if city not in reachable_cities:
                unreachable_cities.append(city)
        if unreachable_cities:
            result.append([gas_storage, unreachable_cities])

    return result
