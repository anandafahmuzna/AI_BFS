from collections import deque

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    return None


graph = {
    'Rumah': ['Warung', 'Gang Belakang'],
    'Warung': ['Rumah', 'Taman'],
    'Gang Belakang': ['Rumah', 'Taman'],
    'Taman': ['Warung', 'Gang Belakang', 'Sekolah'],
    'Sekolah': ['Taman']
}

start_node = 'Rumah'
goal_node = 'Sekolah'

result = bfs(graph, start_node, goal_node)

if result:
    print("Jalur tercepat ditemukan:")
    print(" -> ".join(result))
else:
    print("Jalur tidak ditemukan.")
