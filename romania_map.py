
import math

COORDS = {
    "Arad": (46.1866, 21.3123),
    "Zerind": (46.6225, 21.5174),
    "Oradea": (47.0465, 21.9189),
    "Sibiu": (45.7983, 24.1256),
    "Timisoara": (45.7489, 21.2087),
    "Lugoj": (45.6910, 21.9035),
    "Mehadia": (44.9042, 22.3645),
    "Drobeta": (44.6369, 22.6597),
    "Craiova": (44.3302, 23.7949),
    "Rimnicu Vilcea": (45.0997, 24.3693),
    "Fagaras": (45.8416, 24.9731),
    "Pitesti": (44.8565, 24.8692),
    "Bucharest": (44.4268, 26.1025),
    "Giurgiu": (43.9037, 25.9699),
    "Urziceni": (44.7165, 26.6414),
    "Hirsova": (44.6893, 27.9457),
    "Eforie": (44.0584, 28.6330),
    "Vaslui": (46.6407, 27.7276),
    "Iasi": (47.1585, 27.6014),
    "Neamt": (46.9275, 26.3708),
}

ROADS = [
    ("Oradea", "Zerind", 71),
    ("Oradea", "Sibiu", 151),
    ("Zerind", "Arad", 75),
    ("Arad", "Sibiu", 140),
    ("Arad", "Timisoara", 118),
    ("Timisoara", "Lugoj", 111),
    ("Lugoj", "Mehadia", 70),
    ("Mehadia", "Drobeta", 75),
    ("Drobeta", "Craiova", 120),
    ("Craiova", "Rimnicu Vilcea", 146),
    ("Craiova", "Pitesti", 138),
    ("Sibiu", "Rimnicu Vilcea", 80),
    ("Sibiu", "Fagaras", 99),
    ("Rimnicu Vilcea", "Pitesti", 97),
    ("Fagaras", "Bucharest", 211),
    ("Pitesti", "Bucharest", 101),
    ("Bucharest", "Giurgiu", 90),
    ("Bucharest", "Urziceni", 85),
    ("Urziceni", "Hirsova", 98),
    ("Urziceni", "Vaslui", 142),
    ("Hirsova", "Eforie", 86),
    ("Vaslui", "Iasi", 92),
    ("Iasi", "Neamt", 87),
]

2 mapa_romenia = {
13 'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
14 'Zerind': [('Arad', 75), ('Oradea', 71)],
15 'Oradea': [('Zerind', 71), ('Sibiu', 151)],
16 'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99),
17 ('Rimnicu Vilcea', 80)],
18 'Timisoara': [('Arad', 118), ('Lugoj', 111)],
19 'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
20 'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
21 'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
22 'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
23 'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
24 'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
25 'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
26 'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90),
27 ('Urziceni', 85)],
28 'Giurgiu': [('Bucharest', 90)],
29 'Urziceni': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
30 'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
31 'Eforie': [('Hirsova', 86)],
32 'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
33 'Iasi': [('Vaslui', 92), ('Neamt', 87)],
34 'Neamt': [('Iasi', 87)],
35 


# def build_graph():
#     graph = {city: {} for city in COORDS}
#     for a, b, cost in ROADS:
#         graph[a][b] = cost
#         graph[b][a] = cost
#     return graph
#
#
# GRAPH = build_graph()


# def haversine_km(a, b):
#     lat1, lon1 = map(math.radians, COORDS[a])
#     lat2, lon2 = map(math.radians, COORDS[b])
#     h = (math.sin((lat2 - lat1) / 2) ** 2
#          + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2)
#     return 2 * 6371 * math.asin(math.sqrt(h))
#

# if __name__ == "__main__":
    # for city, neighbors in GRAPH.items():
    #     print(f"{city} {COORDS[city]}: {neighbors}")
    # print("\nEdges where haversine > road cost (inadmissible for A*):")
    # for a, b, cost in ROADS:
    #     d = haversine_km(a, b)
    #     if d > cost:
    #         print(f"  {a} - {b}: road={cost} straight={d:.0f}")
