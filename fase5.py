from map import CITIES, H_BUCHAREST

def a_star(inicio, objetivo):
    fronteira = [(H_BUCHAREST[inicio], 0, inicio, [inicio])]
    explorados = set()

    while fronteira:
        fronteira.sort(key=lambda x: x[0])
        _, g_atual, cidade, caminho = fronteira.pop(0)

        if cidade == objetivo:
            return caminho, g_atual

        if cidade in explorados:
            continue
        explorados.add(cidade)

        for vizinho, custo_estrada in CITIES[cidade]['roads']:
            if vizinho in explorados:
                continue

            novo_g = g_atual + custo_estrada
            novo_f = novo_g + H_BUCHAREST[vizinho]
            fronteira.append((novo_f, novo_g, vizinho, caminho + [vizinho]))

    return None, float('inf')

caminho, custo = a_star('Arad', 'Bucharest')
print(f"Caminho encontrado: {' -> '.join(caminho)}")
print(f"Custo total do caminho: {custo} km")
print(f"Passos: {len(caminho)-1} estradas")