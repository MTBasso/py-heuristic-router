from map import CITIES, H_BUCHAREST

def mostrar_fronteira(fronteira):
    partes = []
    for f, _, cidade, _ in fronteira:
        partes.append(f"{cidade}  (f={f})")
    return (f'  Fronteira: {", ".join(partes)}')

def expandir(no, explorados):
    _, g_atual, cidade_atual, caminho = no
    fronteiras = []
    for vizinho, custo_estrada in CITIES[cidade_atual]['roads']:
        if vizinho  in explorados:
            continue

        novo_g = g_atual + custo_estrada
        novo_f = novo_g + H_BUCHAREST[vizinho]
        novo_caminho = caminho + [vizinho]
        no_vizinho = (novo_f, novo_g, vizinho, novo_caminho)
        fronteiras.append(no_vizinho)
    return fronteiras

inicio = 'Arad'
fronteira = [(H_BUCHAREST[inicio], 0, inicio, [inicio])]
explorados = set()

for rodada in range(3):
    fronteira.sort(key=lambda x: x[0])
    no = fronteira.pop(0)
    cidade = no[2]
    explorados.add(cidade)
    print(f"\nRodada {rodada+1}: expandindo {cidade} com f = {no[0]}, g = {no[1]}")
    fronteira += expandir(no, explorados)
    print(mostrar_fronteira(fronteira))
    print(f"  Explorados: {sorted(explorados)}")