import heapq
from itertools import count

def a_star_search(graph, heuristics, start, goal): 
    pq = []
    heapq.heappush(pq, (0 + heuristics[start], start, [start], 0))
    visited = set()

    while pq:
        f, current, path, g = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path, g

        for neighbor, cost in graph[current].items():
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristics[neighbor]
                heapq.heappush(pq, (new_f, neighbor, path + [neighbor], new_g))

    return None, float('inf')


graph = {
    'Home': {'Mirpur Road': 0.9, 'Town Hall': 0.49},
    'Mirpur Road': {'Home': 0.9, 'Museum': 1.28, 'Asad Gate': 0.5},
    'Asad Gate': {'Mirpur Road': 0.5, 'Arong': 0.22, 'Town Hall': 0.78},
    'Town Hall': {'Home': 0.49, 'Arong': 1.3, 'Asad Gate': 0.78},
    'Arong': {'Asad Gate': 0.22, 'Manik Mia Ave': 0.97, 'Town Hall': 1.3, 'Panthapath': 0.88},
    'Museum': {'Mirpur Road': 1.28, 'Manik Mia Ave': 0.69, 'Bijoy Soroni': 0.57},
    'Manik Mia Ave': {'Arong': 0.97, 'Museum': 0.69, 'Farmgate': 0.68},
    'Panthapath': {'Arong': 0.88, 'Green Road': 0.97},
    'Green Road': {'Panthapath': 0.97, 'UAP': 0.46},
    'Bijoy Soroni': {'Museum': 0.57, 'Farmgate': 0.65},
    'Farmgate': {'Bijoy Soroni': 0.65, 'Manik Mia Ave': 0.68, 'UAP': 0.39},
    'UAP': {'Farmgate': 0.39, 'Green Road': 0.46}
}

heuristics = {
    'Home': 2.97, 'Town Hall': 2.67, 'Mirpur Road': 2.06, 'Asad Gate': 1.86,
    'Arong': 1.68, 'Museum': 1.17, 'Bijoy Soroni': 1.04, 'Manik Mia Ave': 0.67,
    'Farmgate': 0.38, 'Panthapath': 1.29, 'Green Road': 0.47, 'UAP': 0.0
}

start, goal = 'Home', 'UAP'
path, cost = a_star_search(graph, heuristics, start, goal)  
if path:
    print("Optimal Path:", " -> ".join(path))
    print(f"Total Cost: {cost:.2f} km")
else:
    print(f"No path found from {start} to {goal}.")
