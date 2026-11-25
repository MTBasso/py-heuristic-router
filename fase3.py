from map import CITIES, H_BUCHAREST


inicio = 'Arad'
g = 0
h = H_BUCHAREST[inicio]
no_inicial = (g+ h , g, inicio, [inicio])
fronteira = [no_inicial]
print(f"Fronteira inicial: {fronteira}")

no = fronteira.pop(0)
f_atual, g_atual, cidade_atual, caminho = no
print(f"\nNo retirado: {no}")
print(f"f = {(f_atual):<5} | g = {(g_atual):<5} | cidade = {(cidade_atual):<5} | caminho = {caminho}")
print(f"fronteira agora: {fronteira}")

for vizinho, custo_estrada in CITIES[cidade_atual]['roads']:
    novo_g = g_atual + custo_estrada
    novo_h = H_BUCHAREST[vizinho]
    novo_f = novo_g + novo_h
    novo_caminho = caminho + [vizinho]
    no_vizinho = (novo_f, novo_g, vizinho, novo_caminho)
    fronteira.append(no_vizinho)

print()
print("fronteira depois de expandir Arad:")
for no in fronteira:
    print(f'    {no}')

fronteira.sort(key=lambda x: x[0])
print()
print("fronteira depois de ordenar por f(0 da tupla):")
for no in fronteira:
    print(f'    {no}')

proximo = fronteira.pop(0)
print()
print(f"Proximo no a ser expandido: {proximo[2]} com f = {proximo[0]}")