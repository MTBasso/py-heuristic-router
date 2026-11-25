from map import CITIES, H_BUCHAREST

def custo_da_estrada(cidade1, cidade2):
    for vizinho in cidade1["neighbours"]:
        if vizinho["name"] == cidade2["name"]:
            return vizinho["distance"]
    return f"Estrada não encontrada entre {cidade1['name']} e {cidade2['name']}"

def custo_do_caminho(cidades):
    custo_total = 0
    for i in range(len(cidades) - 1):
        custo_total += custo_da_estrada(cidades[i], cidades[i + 1])
    return custo_total

def mostrar_g_h_f(caminho):
    print(f"    {"cidade":<15} {"g(n)":>5} {"h(n)":>5} {"f(n)":>5}")
    for cidade in caminho:

        g = custo_do_caminho(caminho[:caminho.index(cidade) + 1])
        h = H_BUCHAREST[cidade["name"]]
        f = g + h
        print(f"    {cidade['name']:<15} {g:>5} {h:>5} {f:>5}")


print(f"Arad -> Sibiu custa {custo_da_estrada(CITIES['Arad'], CITIES['Sibiu'])} km")
print(f"{custo_da_estrada(CITIES['Arad'], CITIES['Bucharest'])}")

por_fagaras = [CITIES["Arad"], CITIES["Sibiu"], CITIES["Fagaras"], CITIES["Bucharest"]]
por_pitesti = [CITIES["Arad"], CITIES["Sibiu"], CITIES["Rimnicu Vilcea"], CITIES["Pitesti"], CITIES["Bucharest"]]
print()
print(f"Caminho por Fagaras -> {', '.join([cidade['name'] for cidade in por_fagaras])}")
print(f"Custo do caminho por Fagaras = {custo_do_caminho(por_fagaras)} km")
print(f"Caminho por Pitesti -> {', '.join([cidade['name'] for cidade in por_pitesti])}")
print(f"Custo do caminho por Pitesti = {custo_do_caminho(por_pitesti)} km")

print()
print("valores ao longo do caminho por Fagaras:")
mostrar_g_h_f(por_fagaras)
print()
print("valores ao longo do caminho por Pitesti:")
mostrar_g_h_f(por_pitesti)