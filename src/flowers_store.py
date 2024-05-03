import csv


def create_graph(path_to_file) -> dict:
    graph = {}

    with open(path_to_file) as file:
        reader = csv.reader(file)
        farms = next(reader)
        stores = next(reader)

        start_point = farms[0]
        end_point = stores[0]

        if len(farms) > 1:
            start_point = "VirtualStartPoint"
            graph[start_point] = {}
        if len(stores) > 1:
            end_point = "VirtualEndPoint"
            graph[end_point] = {}

        for farm in farms:
            graph[farm] = {}
            if start_point != farms[0]:
                graph[start_point][farm] = float("inf")
        for store in stores:
            graph[store] = {}
            if end_point != stores[0]:
                graph[store][end_point] = float("inf")

        for origin, destination, length in reader:
            if not origin in graph:
                graph[origin] = {}
            if not destination in graph:
                graph[destination] = {}
            graph[origin][destination] = int(length)

    return graph, start_point, end_point


def dfs(graph, start_point, end_point, path_flow=float("inf"), reached_end=False, visited=None, parent=None):
    if visited is None:
        visited = set()
    visited.add(start_point)

    if start_point == end_point:
        reached_end = True
    if parent:
        path_flow = min(path_flow, graph[parent][start_point])

    for neighbor in graph[start_point]:
        if neighbor in visited:
            continue
        if graph[start_point][neighbor] is None:
            continue
        _path_flow, reached_end = dfs(
            graph, neighbor, end_point, path_flow, reached_end, visited, start_point
        )
        if reached_end:
            path_flow = min(_path_flow, path_flow)
            break

    if parent is None:
        return path_flow
    if not reached_end:
        return float("inf"), reached_end

    graph[parent][start_point] -= path_flow

    if graph[parent][start_point] == 0:
        graph[parent][start_point] = None

    return path_flow, reached_end


def get_max_flow(path_to_file: str) -> int:
    graph, start_point, end_point = create_graph(path_to_file)
    result = 0
    path_flow = 0

    while path_flow != float("inf"):
        result += path_flow
        path_flow = dfs(graph, start_point, end_point)

    return result
