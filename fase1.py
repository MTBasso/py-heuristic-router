
from map import ROADS, H_BUCHAREST, get_neighbours

# print(f"quantidade de cidades no mapa: {len(ROADS)}")
# print(f"quantidade de valores h(n): {len(H_BUCHAREST)} \n")

# print(f"tipo roads: {type(ROADS)} \nROADS: {ROADS}\n")
# print(f"tipo h_bucharest: {type(H_BUCHAREST)} \nH_BUCHAREST: {H_BUCHAREST}\n")
# print(f"tipo vizinhos de Arad: {type(ROADS["Arad"])} \n")
print(f"vizinhos de Arad: {get_neighbours("Arad")}")