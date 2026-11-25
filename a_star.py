from map import CITIES, H_BUCHAREST

def resume_fronteira(fronteira):
    return ', '.join([f"{cidade}({f})" for f, _, cidade, _ in fronteira])

def a_star(inicio, objetivo, mostrar=False):
    fronteira = [(H_BUCHAREST[inicio], 0, inicio, [inicio])]
    explorados = set()
    i = 0

    if mostrar:
        print(f"--- Busca A* de {inicio} para {objetivo} ---")

    while fronteira:
        i += 1
        fronteira.sort(key=lambda x: x[0])
        _, g_atual, cidade, caminho = fronteira.pop(0)

        f_proximo = fronteira[0][0] if fronteira else 'N/A'

        if mostrar:
            print(
                f"Iteração {i}: expandindo {cidade} com f = {f_proximo}, g = {g_atual}, h = {H_BUCHAREST[cidade]}\n"
                f"  Fronteira: {resume_fronteira(fronteira)}\n"
                f"  Explorados: {sorted(explorados)}"
            )

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

        if mostrar:
            print(f"  Fronteira após expandir {cidade}: {resume_fronteira(fronteira)}\n")

def a_star_completo():
    print("\nExecutando A* para todos os pares de cidades e mostrando apenas o caminho completo")
    resultados = []
    for cidade_origem in CITIES.keys():
        for cidade_destino in CITIES.keys():
            if cidade_origem != cidade_destino:
                caminho, custo = a_star(cidade_origem, cidade_destino, mostrar=False)
                resultados.append(
                    f"{cidade_origem} -> {cidade_destino}: {' -> '.join(caminho)} (Custo: {custo} km)"
                )
    print('\n'.join(resultados))

def main():
    caminho, custo = a_star('Arad', 'Bucharest')

    print("\n---RESULTADO---")
    if caminho is None:
        print("Nenhum caminho encontrado.")
    else:
        print(
            f"\nCaminho encontrado: {' -> '.join(caminho)}\n"
            f"\nCusto real total: {custo} km em {len(caminho)-1} passos"
        )

    if caminho is not None and custo != 418 and len(caminho) - 1 == 4:
        print("\nO caminho encontrado não é o ótimo. O custo ótimo é 418 km em 4 passos.")

    # A* COMPLETO
    # print("\nExecutando A* completo:")
    # a_star_completo()

if __name__ == "__main__":
    main()
