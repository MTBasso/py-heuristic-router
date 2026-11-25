from map import CITIES, H_BUCHAREST

print(f"Quantidade de cidades no mapa: {len(CITIES)}")
print(f"Quantidade de h(n) calculadas: {len(H_BUCHAREST)}")


arad = CITIES["Arad"]

print(f"\nVizinhos de Arad: {len(arad['neighbours'])}")
for city in arad["neighbours"]:
    print(f"    {city['name']}")


print(f"\nPrimeira estrada que sai de Arad: {arad['neighbours'][0]['name']}")
print(f"    Distância em km: {arad['neighbours'][0]['distance']}")


print(f"\nEstradas que saem de Arad: ")
for neighbour in arad["neighbours"]:
    print(f"    {neighbour['text_value']} km")


print(f"Numero de estradas de cada cidade:")
for city in CITIES.values():
    print(f"    {city['name']:<15}: {len(city['neighbours'])} estradas")

print(f"\nh(Arad) = {H_BUCHAREST['Arad']} km em linha ate Bucareste")
print(f"\npara cada vizinho de arad: custo da estrad e h(vizinho)")
for city in arad["neighbours"]:
    print(f"    {city['name']:<10}: custo da estrada = {city['distance']:>3} km, h({city['name']}) = {H_BUCHAREST[city['name']]:>3} km")