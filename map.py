
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

ROADS = {
 'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
 'Zerind': [('Arad', 75), ('Oradea', 71)],
 'Oradea': [('Zerind', 71), ('Sibiu', 151)],
 'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99),
 ('Rimnicu Vilcea', 80)],
 'Timisoara': [('Arad', 118), ('Lugoj', 111)],
 'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
 'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
 'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
 'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
 'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
 'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
 'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
 'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90),
 ('Urziceni', 85)],
 'Giurgiu': [('Bucharest', 90)],
 'Urziceni': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
 'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
 'Eforie': [('Hirsova', 86)],
 'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
 'Iasi': [('Vaslui', 92), ('Neamt', 87)],
'Neamt': [('Iasi', 87)],
}

H_BUCHAREST = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374,
}

def get_neighbours(city: str) -> list:
    neighbours = []
    for dest, dist in ROADS[city]:
        neighbours.append(f"{city} -> {dest} ({dist})")
    return neighbours
